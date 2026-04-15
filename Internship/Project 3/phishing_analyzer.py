# ============================================================
#  DecodeLabs | Cyber Security | Project 3
#  Phishing Awareness Analyzer — Triage Toolkit
#  Batch: 2026
# ============================================================
#
#  Triage Decision Model:
#    0-2  flags  → SAFE       → Close
#    3-4  flags  → SUSPICIOUS → Warn User
#    5+   flags  → MALICIOUS  → Block & Escalate
#
# ============================================================

import re

# ── Red Flag Definitions ─────────────────────────────────────
# Each entry: (pattern, flag_name, explanation, severity)
# severity: 1 = low, 2 = medium, 3 = high

KEYWORD_FLAGS = [
    # Urgency triggers
    (r'\burgent\b',           "Urgency keyword",         "Creates artificial time pressure to bypass rational thinking.", 2),
    (r'\bimmediately\b',      "Urgency keyword",         "Forces a fight-or-flight response — a classic cognitive exploit.", 2),
    (r'\bact now\b',          "Urgency keyword",         "Pressures victim to skip verification steps.", 2),
    (r'\bexpires?\b',         "Deadline pressure",       "Fake deadlines are used to create urgency and panic.", 2),
    (r'\b24 hours?\b',        "Deadline pressure",       "Specific time windows increase perceived urgency.", 2),
    (r'\blimited time\b',     "Deadline pressure",       "Scarcity tactic to force impulsive action.", 2),

    # Authority triggers
    (r'\bverify your account\b',    "Account verification request", "Phishing emails often fake account alerts to harvest credentials.", 3),
    (r'\bconfirm your (password|details|information|identity)\b', "Credential request", "Legitimate services never ask for passwords via email.", 3),
    (r'\bupdate your (billing|payment|card|info)\b', "Payment detail request", "A common Business Email Compromise (BEC) tactic.", 3),
    (r'\byour account (has been|will be) (suspended|locked|disabled|terminated)\b', "Account suspension threat", "Fear-based trigger to force immediate action without verification.", 3),
    (r'\bwire transfer\b',    "Wire transfer request",   "Classic Business Email Compromise (BEC) — CEO fraud scenario.", 3),
    (r'\bstrictly confidential\b', "Secrecy demand",     "Red Flag 5: Demands secrecy to prevent the victim from consulting others.", 3),
    (r'\bdo not (discuss|tell|share)\b', "Secrecy demand", "Isolating the victim from peers is a core social engineering tactic.", 3),
    (r'\bbypass (standard|normal|security) (procedure|protocol|process)\b', "Procedure bypass", "Requesting victims skip security protocols is a critical red flag.", 3),

    # Fear / Greed triggers
    (r'\bcongratulations\b',  "Prize/reward lure",       "Unexpected rewards exploit greed — a classic phishing hook.", 2),
    (r'\byou (have won|are selected|are a winner)\b', "Prize lure", "Fabricated winnings are used to lower the victim's guard.", 2),
    (r'\bfree (gift|reward|prize|iphone|laptop)\b', "Free item lure", "Greed-based lure designed to override rational decision-making.", 2),
    (r'\blegal action\b',     "Threat of legal action",  "Fear/Greed trigger — threatening consequences to force compliance.", 3),
    (r'\bIRS|EFCC|police|FBI\b', "Authority impersonation", "Impersonating law enforcement to create extreme fear.", 3),

    # Curiosity triggers
    (r'\bsee what .{0,30} said about you\b', "Curiosity bait", "Exploits the human need to fill knowledge gaps.", 2),
    (r'\bsomeone shared .{0,20} with you\b', "Curiosity bait", "Bait designed to trigger an instinctive click response.", 2),

    # Sensitive info requests
    (r'\b(enter|provide|submit|send) your (password|pin|ssn|otp|code|credentials)\b', "Credential harvesting", "No legitimate service requests credentials via email.", 3),
    (r'\bmfa|one.time (password|code|pin)\b', "MFA code request",     "Red Flag 6: Attackers request MFA codes to bypass 2FA in real-time.", 3),
]

DOMAIN_FLAGS = [
    # Suspicious domain patterns
    (r'http[s]?://[^\s]*\d+\.\d+\.\d+\.\d+', "IP address URL",        "Legitimate services use domain names, not raw IP addresses.", 3),
    (r'http[s]?://[^\s]*(login|secure|verify|update|account)[^\s]*\.[a-z]{2,}', "Suspicious login domain", "Domains containing security keywords are often spoofed.", 3),
    (r'http[s]?://[^\s]*-[^\s]*\.(com|net|org)',  "Hyphenated domain", "Combosquatting: adding words like 'secure-login' to brand names.", 2),
    (r'http[s]?://[^\s]*\.(xyz|tk|ml|ga|cf|gq)', "Suspicious TLD",    "Free or uncommon TLDs (.xyz, .tk) are heavily abused by attackers.", 3),
    (r'http[s]?://[^\s]{60,}',                    "Excessively long URL","Long URLs are used to bury the malicious root domain.", 2),
    (r'bit\.ly|tinyurl|t\.co|goo\.gl|ow\.ly',     "Shortened URL",    "URL shorteners hide the true destination — always expand before clicking.", 2),
    (r'http[s]?://[^\s]*@[^\s]*',                  "URL with @ symbol","Anything before @ in a URL is ignored — a common obfuscation trick.", 3),
]

SENDER_FLAGS = [
    (r'from:.*<[^>]*gmail\.com>',    "Free email sender",    "Legitimate companies use corporate domains, not gmail.com.", 2),
    (r'from:.*<[^>]*yahoo\.com>',    "Free email sender",    "Legitimate companies use corporate domains, not yahoo.com.", 2),
    (r'reply-to:.*(?!from:)',        "Reply-To mismatch",    "A Reply-To address different from From is a display name spoofing indicator.", 3),
    (r'from:.*support.*<[^>]*(?!support)[^>]*>',  "Sender domain mismatch", "Display name says 'Support' but actual domain does not match.", 3),
]

ATTACHMENT_FLAGS = [
    (r'\.(exe|js|vbs|scr|bat|cmd|ps1|iso|lnk)\b', "Dangerous attachment extension", "Red Flag 4: These file types can execute malicious code.", 3),
    (r'\.(zip|rar|7z)\b',                          "Compressed archive attachment",  "Archives are used to bypass email filters scanning for malicious files.", 2),
    (r'security.update|invoice|payment|receipt',   "Suspicious attachment name",     "Attackers name files to appear as routine business documents.", 2),
]


def scan_text(text: str) -> list:
    """Scans message text for phishing red flags. Returns list of findings."""
    findings = []
    text_lower = text.lower()

    for pattern, flag, explanation, severity in KEYWORD_FLAGS:
        if re.search(pattern, text_lower):
            findings.append({
                "category"   : "Content / Keyword",
                "flag"       : flag,
                "explanation": explanation,
                "severity"   : severity,
                "match"      : re.search(pattern, text_lower).group()
            })

    for pattern, flag, explanation, severity in DOMAIN_FLAGS:
        if re.search(pattern, text, re.IGNORECASE):
            findings.append({
                "category"   : "URL / Domain",
                "flag"       : flag,
                "explanation": explanation,
                "severity"   : severity,
                "match"      : re.search(pattern, text, re.IGNORECASE).group()
            })

    for pattern, flag, explanation, severity in SENDER_FLAGS:
        if re.search(pattern, text, re.IGNORECASE):
            findings.append({
                "category"   : "Sender / Header",
                "flag"       : flag,
                "explanation": explanation,
                "severity"   : severity,
                "match"      : re.search(pattern, text, re.IGNORECASE).group()
            })

    for pattern, flag, explanation, severity in ATTACHMENT_FLAGS:
        if re.search(pattern, text, re.IGNORECASE):
            findings.append({
                "category"   : "Attachment",
                "flag"       : flag,
                "explanation": explanation,
                "severity"   : severity,
                "match"      : re.search(pattern, text, re.IGNORECASE).group()
            })

    return findings


def triage(findings: list) -> tuple:
    """
    Applies the triage decision model.
    Returns (verdict, action, risk_score)
    """
    high   = sum(1 for f in findings if f["severity"] == 3)
    medium = sum(1 for f in findings if f["severity"] == 2)
    score  = (high * 3) + (medium * 2)

    if high >= 2 or score >= 6:
        return "🔴 MALICIOUS",  "BLOCK domain & ESCALATE to security team immediately.", score
    elif high == 1 or score >= 3:
        return "🟡 SUSPICIOUS", "WARN user. Do not click links. Verify sender via phone.", score
    else:
        return "🟢 SAFE",       "CLOSE. No significant threat indicators found.",         score


def display_report(text: str, findings: list) -> None:
    """Prints the full triage report."""
    verdict, action, score = triage(findings)

    print("\n" + "=" * 60)
    print("  🎣 PHISHING TRIAGE REPORT — DecodeLabs Project 3")
    print("=" * 60)
    print(f"  Risk Score : {score}")
    print(f"  Verdict    : {verdict}")
    print(f"  Action     : {action}")
    print("-" * 60)

    if not findings:
        print("  No phishing indicators detected.")
    else:
        print(f"  Red Flags Found: {len(findings)}\n")
        for i, f in enumerate(findings, 1):
            sev_label = {3: "HIGH", 2: "MEDIUM", 1: "LOW"}[f["severity"]]
            print(f"  [{i}] ⚠  {f['flag']}  [{sev_label}]")
            print(f"      Category : {f['category']}")
            print(f"      Matched  : \"{f['match']}\"")
            print(f"      Why      : {f['explanation']}")
            print()

    print("-" * 60)
    print("  Golden Rule: PAUSE → VERIFY → REPORT")
    print("  Never click links. Verify via out-of-band channel.")
    print("=" * 60 + "\n")


SAMPLE_EMAILS = {
    "1": {
        "label": "BEC — CEO Wire Transfer (MALICIOUS)",
        "text": """From: CEO Name <ceo.urgent@executive-update.com>
Subject: IMMEDIATE ACTION REQUIRED: Transfer Authorization

URGENT: Process the attached wire transfer instruction immediately.

This is critical and must remain STRICTLY CONFIDENTIAL.
Do not discuss with anyone. Bypass standard procedure.

I lost my wallet at the airport. Need you to wire transfer funds
for my flight immediately. This expires in 24 hours.

Thank you."""
    },
    "2": {
        "label": "Fake Microsoft Alert (SUSPICIOUS)",
        "text": """From: Microsoft Support <support@logins-updates.com>
Subject: FW: Urgent: Your Account Security Alert

Your Microsoft account has been suspended.
Please verify your account immediately to avoid permanent loss.

Click here to confirm your password:
http://microsoft-secure-login.verify-account.xyz/update

This link expires in 24 hours."""
    },
    "3": {
        "label": "Normal Internal Email (SAFE)",
        "text": """From: Project Manager <sarah.lee@company.com>
Subject: Q3 Project Status Update — Non-Urgent

Hi Team,

Please review the attached project status for Q3 at your earliest convenience.
No immediate action is required.

Thanks,
Sarah

Attachment: Q3_Status.pdf"""
    }
}


def main():
    print("\n🛡️  DecodeLabs | Cyber Security — Project 3")
    print("    Phishing Awareness Analyzer\n")

    while True:
        print("Options:")
        print("  [1] Analyze a sample phishing email")
        print("  [2] Analyze a sample suspicious email")
        print("  [3] Analyze a sample safe email")
        print("  [4] Paste your own email / message to analyze")
        print("  [5] Quit")
        choice = input("\nChoose an option (1-5): ").strip()

        if choice in ("1", "2", "3"):
            sample = SAMPLE_EMAILS[choice]
            print(f"\n  Sample: {sample['label']}")
            print("  " + "-" * 56)
            print(sample["text"])
            findings = scan_text(sample["text"])
            display_report(sample["text"], findings)

        elif choice == "4":
            print("\n  Paste your email/message below.")
            print("  When done, type END on a new line and press Enter:\n")
            lines = []
            while True:
                line = input()
                if line.strip().upper() == "END":
                    break
                lines.append(line)
            text = "\n".join(lines)
            if text.strip():
                findings = scan_text(text)
                display_report(text, findings)
            else:
                print("  ⚠️  No text entered.\n")

        elif choice == "5":
            print("\n  Session ended. Stay vigilant! 🛡️\n")
            break

        else:
            print("  ⚠️  Invalid option. Enter 1–5.\n")


if __name__ == "__main__":
    main()

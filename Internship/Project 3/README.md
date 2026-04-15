# 🎣 Phishing Awareness Analyzer — Triage Toolkit
> DecodeLabs Cyber Security Industrial Training | Batch 2026 | Project 3

---

## 📌 Overview

This project builds a **Phishing Triage Toolkit** — a Python-based engine and interactive browser tool that analyzes emails and messages for phishing indicators, classifies the threat level, and delivers a clear, actionable verdict.

Project 3 moves from technical cryptography into **human-layer security** — the most exploited attack surface in cybersecurity. As the training brief states: *"The modern cybersecurity perimeter is no longer the network firewall. It is the user."*

---

## 🎯 Project Goals

- Analyze sample emails and messages for phishing red flags
- Identify suspicious keywords, URLs, sender anomalies, and attachments
- Classify each threat: Safe / Suspicious / Malicious
- Deliver actionable triage outcomes: Close / Warn User / Block & Escalate
- Demonstrate understanding of social engineering psychology

---

## 🧠 The Threat Landscape

| Statistic | Source |
|-----------|--------|
| 80% of security breaches involve phishing | Verizon DBIR |
| 40% of employees fall for simulated campaigns | Citadelo Simulation |
| Average time to first click after campaign launch | 82 seconds |

Phishing has evolved from mass spray-and-pray emails to **AI-driven, highly targeted psychological exploits** — spear phishing that references your colleagues by name, deepfake executive voice calls, and QR codes that bypass desktop URL filters entirely.

---

## 🗂️ Project Structure

```
phishing_analyzer.py       # Main Python CLI triage tool
phishing_analyzer.html     # Interactive browser-based analyzer
README.md                  # This file
```

---

## 🚦 Triage Decision Model

Every analyzed message receives one of three verdicts:

| Verdict | Trigger Condition | Action |
|---------|-------------------|--------|
| 🟢 **SAFE** | Score < 3, no high-severity flags | Close — no action needed |
| 🟡 **SUSPICIOUS** | 1 high flag OR score 3–5 | Warn user — verify via out-of-band channel |
| 🔴 **MALICIOUS** | 2+ high flags OR score ≥ 6 | Block domain & escalate to security team |

**Scoring System:**
- High severity flag = 3 points
- Medium severity flag = 2 points
- Low severity flag = 1 point

---

## ⚠️ The 11 Categories of Red Flags

### Content / Keyword Flags
| Red Flag | Severity | Description |
|----------|----------|-------------|
| Urgency keywords | MEDIUM | "Urgent", "immediately", "act now" — triggers fight-or-flight response |
| Deadline pressure | MEDIUM | "24 hours", "expires soon" — eliminates time to verify |
| Account suspension threat | HIGH | Fear trigger to force immediate credential submission |
| Wire transfer request | HIGH | Classic BEC (Business Email Compromise) — CEO fraud |
| Secrecy demand | HIGH | "Do not discuss" — isolates victim from peers |
| Procedure bypass | HIGH | "Skip standard process" — removes safety checks |
| Prize / reward lure | MEDIUM | Greed trigger — "You have won" |
| Credential harvesting | HIGH | Direct request for passwords, OTP, MFA codes |
| Authority impersonation | HIGH | Impersonating IRS, FBI, IT department |

### URL / Domain Flags
| Red Flag | Severity | Description |
|----------|----------|-------------|
| IP address URL | HIGH | Real domains, not raw IPs like `http://192.168.1.1` |
| Suspicious login domain | HIGH | Domains like `microsoft-secure-login.xyz` |
| Hyphenated domain (Combosquatting) | MEDIUM | `yourcompany-secure-login.com` |
| Suspicious TLD | HIGH | `.xyz`, `.tk`, `.ml` — heavily abused free TLDs |
| Shortened URL | MEDIUM | Hides true destination — always expand before clicking |
| URL with @ symbol | HIGH | Everything before @ is ignored by the browser |

### Sender / Header Flags
| Red Flag | Severity | Description |
|----------|----------|-------------|
| Free email domain | MEDIUM | Legitimate companies don't use `@gmail.com` |
| Display name spoofing | HIGH | "CEO Name" displayed but `hacker@gmail.com` underneath |

### Attachment Flags
| Red Flag | Severity | Description |
|----------|----------|-------------|
| Dangerous extension | HIGH | `.exe`, `.js`, `.scr`, `.iso` — executable malware |
| Compressed archive | MEDIUM | Zips used to bypass attachment scanners |

---

## 🧬 Phishing Attack Taxonomy

### By Targeting Level
```
Mass Phishing     →  Generic brand lures (Amazon, PayPal) — ~1% click rate
Spear Phishing    →  Contextual, uses victim's name/colleagues/projects
Whaling           →  Targeting C-suite for wire transfers and M&A documents
```

### By Delivery Channel
| Vector | Method |
|--------|--------|
| Email Phishing | Display name spoofing, lookalike domains |
| Smishing | Malicious SMS disguised as package alerts |
| Vishing | Caller ID spoofing to impersonate IT/government |
| Quishing | QR codes bypassing desktop URL filters |
| TOAD | Callback scams — no links, just a fake support number |
| Deepfake | AI voice/video impersonation of executives |

---

## 🧠 The Psychology Behind Phishing

Attackers weaponize four cognitive triggers:

| Trigger | Example |
|---------|---------|
| **Authority** | Impersonating the CEO, IT dept, or law enforcement |
| **Urgency** | "Account locked in 30 minutes" — triggers fight-or-flight |
| **Curiosity** | "See what your colleague said about you" |
| **Fear / Greed** | Legal threats OR unexpected prize winnings |

Understanding **why** phishing works is as important as knowing what to look for.

---

## 🔎 Domain Spoofing Techniques

| Technique | Example | Detection |
|-----------|---------|-----------|
| **Typosquatting** | `amaz0n.com` | Read the domain character by character |
| **Homoglyph Attack** | `paypal.com` with Cyrillic 'a' | Enable Unicode display in browser |
| **Combosquatting** | `yourcompany-secure-login.com` | Read URL right-to-left to find root domain |
| **Subdomain Trap** | `www.decodelabs.tech.login-update.com` | True root is after the last dot before the path |

**Golden Rule for URLs: Always read right-to-left to find the true root domain.**

---

## 💻 How to Run (Python CLI)

### Requirements
- Python 3.x (no external libraries needed)

```bash
python phishing_analyzer.py
```

### Menu
```
[1] Analyze a sample phishing email        → MALICIOUS demo
[2] Analyze a sample suspicious email      → SUSPICIOUS demo
[3] Analyze a sample safe email            → SAFE demo
[4] Paste your own email / message         → Custom analysis
[5] Quit
```

---

## 🌐 How to Use (Browser Tool)

1. Download `phishing_analyzer.html`
2. Double-click to open in any browser
3. Load a sample email or paste your own
4. Click **Run Triage Analysis**
5. Review the verdict, risk score, and red flag breakdown

---

## 📋 Sample Output

```
============================================================
  🎣 PHISHING TRIAGE REPORT — DecodeLabs Project 3
============================================================
  Risk Score : 18
  Verdict    : 🔴 MALICIOUS
  Action     : BLOCK domain & ESCALATE to security team immediately.
------------------------------------------------------------
  Red Flags Found: 5

  [1] ⚠  Wire transfer request  [HIGH]
      Category : Content / Keyword
      Matched  : "wire transfer"
      Why      : Classic Business Email Compromise (BEC) — CEO fraud scenario.

  [2] ⚠  Secrecy demand  [HIGH]
      Category : Content / Keyword
      Matched  : "strictly confidential"
      Why      : Red Flag 5: Demands secrecy to prevent consulting others.
...
------------------------------------------------------------
  Golden Rule: PAUSE → VERIFY → REPORT
============================================================
```

---

## 🛡️ The Golden Rule of the Human Firewall

```
1. PAUSE    →  Recognize the cognitive trigger (urgency, fear, authority)
2. VERIFY   →  Confirm via out-of-band channel (call a known number — not one in the email)
3. REPORT   →  Don't just delete — reporting lets the security team purge the threat from all inboxes
```

---

## 📚 Key Concepts Learned

- Social engineering psychology (Authority, Urgency, Curiosity, Fear/Greed)
- Phishing taxonomy: Mass → Spear → Whaling → Vishing → Quishing → TOAD → Deepfake
- Domain spoofing techniques: Typosquatting, Homoglyph, Combosquatting, Subdomain traps
- Email header analysis: From vs Reply-To, Display Name Spoofing, SPF/DKIM/DMARC
- Triage methodology: Safe → Close, Suspicious → Warn, Malicious → Block & Escalate
- Regex-based pattern detection in Python

---

## 🛡️ Built With

- **Language:** Python 3 + Vanilla HTML/CSS/JavaScript
- **Libraries:** `re` (Python standard library — no installs needed)
- **Program:** DecodeLabs Cyber Security Industrial Training — Batch 2026
- **Track:** Junior Analyst / Threat Detection

---

> *"Phishing exploits the space between a technical control and a human reaction. By mastering threat taxonomy, identifying technical disguises, and deploying realistic simulations, you are closing that gap."*
> — DecodeLabs Project 3 Brief

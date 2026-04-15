# ============================================================
#  DecodeLabs | Cyber Security | Project 1
#  Password Strength Checker
#  Batch: 2026
# ============================================================

import string

# A small set of commonly leaked / weak passwords (bonus check)
COMMON_PASSWORDS = {
    "password", "123456", "password123", "qwerty", "abc123",
    "letmein", "welcome", "admin", "iloveyou", "monkey",
    "1234567890", "dragon", "master", "sunshine", "princess"
}

def check_password_strength(password: str) -> dict:
    """
    Evaluates a password and returns a detailed strength report.

    Scoring rules (1 point each):
        1. Length >= 8 characters   (< 8 = immediate WEAK, no further checks)
        2. Contains uppercase letter [A-Z]
        3. Contains digit           [0-9]
        4. Contains special symbol  [!@#$%^&*...]
        5. Length >= 12 characters  (bonus for extra length)

    Strength levels:
        0-1 points  → WEAK
        2-3 points  → MEDIUM
        4-5 points  → STRONG
    """

    result = {
        "password"      : password,
        "length"        : len(password),
        "has_upper"     : False,
        "has_digit"     : False,
        "has_symbol"    : False,
        "is_common"     : False,
        "score"         : 0,
        "strength"      : "",
        "feedback"      : []
    }

    # ── Gate check: length must be at least 8 ──────────────────
    if len(password) < 8:
        result["strength"] = "WEAK"
        result["feedback"].append("❌ Too short — minimum 8 characters required.")
        return result

    # ── Common password check ───────────────────────────────────
    if password.lower() in COMMON_PASSWORDS:
        result["is_common"] = True
        result["strength"]  = "WEAK"
        result["feedback"].append("❌ This is a commonly leaked password. Choose something unique.")
        return result

    # ── Pythonic pattern recognition (any + generator) ──────────
    result["has_upper"]  = any(char.isupper()                    for char in password)
    result["has_digit"]  = any(char.isdigit()                    for char in password)
    result["has_symbol"] = any(char in string.punctuation        for char in password)

    # ── Scoring ─────────────────────────────────────────────────
    score = 1                                       # passed length gate

    if result["has_upper"]:
        score += 1
    else:
        result["feedback"].append("⚠️  Add at least one uppercase letter [A-Z].")

    if result["has_digit"]:
        score += 1
    else:
        result["feedback"].append("⚠️  Add at least one digit [0-9].")

    if result["has_symbol"]:
        score += 1
    else:
        result["feedback"].append("⚠️  Add at least one special character [!@#$%^&*].")

    if len(password) >= 12:                         # bonus point
        score += 1

    result["score"] = score

    # ── Classify strength ────────────────────────────────────────
    if score <= 2:
        result["strength"] = "WEAK"
    elif score <= 3:
        result["strength"] = "MEDIUM"
    else:
        result["strength"] = "STRONG"

    if not result["feedback"]:
        result["feedback"].append("✅ Excellent password! All criteria met.")

    return result


def display_report(report: dict) -> None:
    """Prints a formatted strength report to the console."""

    ICONS = {"WEAK": "🔴", "MEDIUM": "🟡", "STRONG": "🟢"}

    print("\n" + "=" * 50)
    print("  🔐 PASSWORD STRENGTH REPORT — DecodeLabs")
    print("=" * 50)
    print(f"  Password : {'*' * len(report['password'])}")
    print(f"  Length   : {report['length']} characters")
    print(f"  Uppercase: {'✔' if report['has_upper']  else '✘'}")
    print(f"  Digit    : {'✔' if report['has_digit']  else '✘'}")
    print(f"  Symbol   : {'✔' if report['has_symbol'] else '✘'}")
    print(f"  Score    : {report['score']} / 5")
    print("-" * 50)
    icon = ICONS.get(report["strength"], "")
    print(f"  Result   : {icon}  {report['strength']}")
    print("-" * 50)
    print("  Feedback:")
    for tip in report["feedback"]:
        print(f"    {tip}")
    print("=" * 50 + "\n")


def main():
    print("\n🛡️  DecodeLabs | Cyber Security — Project 1")
    print("    Password Strength Checker\n")

    while True:
        password = input("Enter a password to check (or 'quit' to exit): ").strip()

        if password.lower() == "quit":
            print("\n  Session ended. Stay secure! 🔒\n")
            break

        if not password:
            print("  ⚠️  No password entered. Try again.\n")
            continue

        report = check_password_strength(password)
        display_report(report)


if __name__ == "__main__":
    main()

# 🛡️ Cyber Security Industrial Training — DecodeLabs Batch 2026

> **Trainee:** Kazeem Habeeb
> **Program:** DecodeLabs Cyber Security Industrial Training
> **Track:** Junior Analyst — Defensive Logic
> **Batch:** 2026

---

## 📌 About This Repository

This repository documents my hands-on journey through the **DecodeLabs Cyber Security Industrial Training Program**. Each project is a practical, real-world milestone built entirely in Python — covering defensive security logic, cryptography, and threat detection.

Every project follows the same structure:
- Python source code (written independently)
- Interactive browser demo (built with AI assistance)
- Detailed README documentation
- LinkedIn post showcasing the work

---

## 🗂️ Project Index

| # | Project | Track | Core Concept | Status |
|---|---------|-------|--------------|--------|
| 1 | [Password Strength Checker](#-project-1--password-strength-checker) | Defensive Logic | String handling, entropy, validation | ✅ Complete |
| 2 | [Caesar Cipher — Encryption & Decryption](#-project-2--caesar-cipher--encryption--decryption) | Cryptography | Modular arithmetic, symmetric encryption | ✅ Complete |
| 3 | [Phishing Awareness Analyzer](#-project-3--phishing-awareness-analyzer) | Threat Detection | Regex, social engineering, triage logic | ✅ Complete |

---

## 🔐 Project 1 — Password Strength Checker

### Overview
A Python program that evaluates any password and classifies it as **WEAK**, **MEDIUM**, or **STRONG** using a 5-point scoring system. Includes a common leaked password blocklist as a bonus security layer.

### Key Requirements Met
- ✅ Check password length (< 8 = instant WEAK gate)
- ✅ Check use of uppercase letters, digits, and symbols
- ✅ Display strength result with detailed feedback
- ✅ Bonus: leaked password blocklist

### Core Logic

```python
# Pythonic approach — using any() with generator expressions
has_upper  = any(char.isupper()             for char in password)
has_digit  = any(char.isdigit()             for char in password)
has_symbol = any(char in string.punctuation for char in password)
```

The course emphasized this Pythonic pattern over verbose manual loops — `any()` short-circuits on the first match, making it both cleaner and faster.

### Scoring System

| Score | Strength | Criteria |
|-------|----------|----------|
| 0–1 | 🔴 WEAK | Failed length gate or too simple |
| 2–3 | 🟡 MEDIUM | Passes some checks |
| 4–5 | 🟢 STRONG | Passes all checks + length ≥ 12 bonus |

### Security Concepts Learned
- **Password entropy** — why length and character variety matter
- **Brute force risk** — passwords under 8 characters are exponentially easier to crack
- **Common password attacks** — why a blocklist is essential even for "strong-looking" passwords
- **Data in RAM (HINNOP)** — Python strings are immutable; sensitive data lingers in heap memory until garbage collection

### Files
```
project-1-password-checker/
├── password_checker.py       # Main Python CLI tool
├── demo.jsx                  # Interactive React demo (AI-assisted)
└── README.md
```

### Sample Output
```
==================================================
  🔐 PASSWORD STRENGTH REPORT — DecodeLabs
==================================================
  Password : ************
  Length   : 12 characters
  Uppercase: ✔    Digit: ✔    Symbol: ✔
  Score    : 5 / 5
--------------------------------------------------
  Result   : 🟢  STRONG
--------------------------------------------------
  Feedback:
    ✅ Excellent password! All criteria met.
==================================================
```

---

## 🔑 Project 2 — Caesar Cipher — Encryption & Decryption

### Overview
A Python implementation of the **Caesar Cipher** — one of history's oldest encryption techniques. Demonstrates the core principles of data confidentiality, symmetric encryption, and cryptographic vulnerability through a full CLI tool with encrypt, decrypt, and brute force modes.

### Key Requirements Met
- ✅ Encrypt user text using Caesar Cipher logic
- ✅ Decrypt encrypted text using the same key
- ✅ Display both encrypted and decrypted output
- ✅ Handle edge cases: spaces, digits, punctuation, mixed case
- ✅ Bonus: brute force mode demonstrating the cipher's vulnerability

### The Math

**Encryption:**
```
E(x) = (x + n) % 26
```

**Decryption:**
```
D(x) = (x - n) % 26
```

Where `x` = character position (A=0 ... Z=25) and `n` = shift key.

### Step-by-Step: Encrypting 'A' with Shift 3

| Step | Operation | Result |
|------|-----------|--------|
| Input | `'A'` | — |
| ASCII | `ord('A')` | `65` |
| Subtract base | `65 - 65` | `0` |
| Add shift | `0 + 3` | `3` |
| Modulo | `3 % 26` | `3` |
| Add base | `3 + 65` | `68` |
| Output | `chr(68)` | `'D'` |

### Core Implementation

```python
def caesar_encrypt(plaintext: str, shift: int) -> str:
    ciphertext = []
    for char in plaintext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - base + shift) % 26 + base)
            ciphertext.append(encrypted_char)
        else:
            ciphertext.append(char)  # spaces, digits, symbols pass through
    return ''.join(ciphertext)

def caesar_decrypt(ciphertext: str, shift: int) -> str:
    return caesar_encrypt(ciphertext, -shift)  # decryption = negative shift
```

**Key insight:** Decryption is just encryption with a negative shift. One line of code captures the entire concept of symmetric cryptography.

### Why the Caesar Cipher Fails

| Vulnerability | Explanation |
|---------------|-------------|
| **Tiny key space** | Only 25 possible keys — brute force takes milliseconds |
| **Pattern preservation** | Letter frequency distribution is maintained in ciphertext, enabling frequency analysis |

This is why modern encryption (AES-256) uses 2^256 possible keys with confusion and diffusion — making brute force computationally impossible.

### The Evolution
```
Caesar Cipher  →  Vigenère Cipher  →  AES-256
(25 keys)         (polyalphabetic)    (2^256 keys)
```

### Files
```
project-2-caesar-cipher/
├── cipher.py                  # Main Python CLI tool
├── cipher_interactive.html    # Interactive browser demo (AI-assisted)
└── README.md
```

### Sample Output
```
============================================================
  🔐 CIPHER REPORT — DecodeLabs Project 2
============================================================
  Shift key   : 3
  Plaintext   : Hello World
  Ciphertext  : Khoor Zruog
  Decrypted   : Hello World
============================================================
```

---

## 🎣 Project 3 — Phishing Awareness Analyzer

### Overview
A Python-based **Phishing Triage Toolkit** that analyzes emails and messages for phishing red flags across four detection categories, scores the threat severity, and delivers a clear actionable verdict. This project moves from technical cryptography into **human-layer security** — the most exploited attack surface in modern cybersecurity.

> *"The modern cybersecurity perimeter is no longer the network firewall. It is the user."* — DecodeLabs Project 3 Brief

### Key Requirements Met
- ✅ Identify suspicious links, domains, and keywords
- ✅ List red flags found in phishing messages with explanations
- ✅ Explain why each message element is unsafe
- ✅ Triage outcome: Safe / Suspicious / Malicious with exact action
- ✅ Bonus: 3 built-in real-world sample emails for demonstration

### Triage Decision Model

| Verdict | Trigger | Action |
|---------|---------|--------|
| 🟢 **SAFE** | Score < 3, no high flags | Close |
| 🟡 **SUSPICIOUS** | 1 high flag OR score 3–5 | Warn User — verify out-of-band |
| 🔴 **MALICIOUS** | 2+ high flags OR score ≥ 6 | Block domain & Escalate |

**Severity scoring:** HIGH flag = 3pts · MEDIUM = 2pts · LOW = 1pt

### Detection Categories

**1. Content / Keyword Flags**
Detects urgency triggers, authority impersonation, secrecy demands, credential requests, wire transfer attempts, deadline pressure, and cognitive bait using `re` pattern matching.

**2. URL / Domain Flags**
Detects IP address links, lookalike/combosquatted domains, suspicious TLDs (`.xyz`, `.tk`), shortened URLs, excessively long URLs, and `@`-embedded URLs.

**3. Sender / Header Flags**
Detects free email domains posing as corporate senders and display name spoofing indicators.

**4. Attachment Flags**
Detects dangerous file extensions (`.exe`, `.js`, `.scr`, `.iso`) and compressed archives used to bypass email filters.

### Core Architecture

```python
def scan_text(text: str) -> list:
    """Scans message for phishing red flags across all categories."""
    findings = []
    for pattern, flag, explanation, severity in KEYWORD_FLAGS:
        if re.search(pattern, text.lower()):
            findings.append({
                "flag": flag, "explanation": explanation,
                "severity": severity,
                "match": re.search(pattern, text.lower()).group()
            })
    # ... URL, sender, attachment checks follow same pattern
    return findings

def triage(findings: list) -> tuple:
    """Applies the triage decision model."""
    high  = sum(1 for f in findings if f["severity"] == 3)
    score = sum(f["severity"] for f in findings)
    if high >= 2 or score >= 6:
        return "🔴 MALICIOUS", "BLOCK domain & ESCALATE immediately."
    elif high == 1 or score >= 3:
        return "🟡 SUSPICIOUS", "WARN user. Verify via out-of-band channel."
    return "🟢 SAFE", "CLOSE. No significant threat indicators found."
```

### The Psychology of Phishing

Attackers weaponize four cognitive triggers that bypass logical verification:

| Trigger | Tactic | Example |
|---------|--------|---------|
| **Authority** | Impersonating C-suite or IT | "Your CEO needs an urgent wire transfer" |
| **Urgency** | Artificial time pressure | "Account locked in 30 minutes" |
| **Curiosity** | Knowledge gap exploitation | "See what your colleague said about you" |
| **Fear / Greed** | Threats or rewards | Legal action OR unexpected prize winnings |

### Phishing Taxonomy
```
Mass Phishing    →  Generic brand lures (~1% click rate)
Spear Phishing   →  Contextual, uses OSINT from LinkedIn/social media
Whaling          →  Targeting C-suite for wire transfers (BEC)
Smishing         →  SMS-based — package alerts, bank notifications
Vishing          →  Caller ID spoofing — fake IT/government calls
Quishing         →  QR codes bypassing desktop URL filters
TOAD             →  Callback scams — no links, just a fake support number
Deepfake         →  AI voice/video impersonation of executives
```

### Domain Spoofing Techniques

| Technique | Example | How to Catch It |
|-----------|---------|-----------------|
| **Typosquatting** | `amaz0n.com` | Read every character carefully |
| **Homoglyph Attack** | `paypal.com` with Cyrillic 'a' | Enable Unicode display |
| **Combosquatting** | `yourcompany-secure-login.com` | Read URL right-to-left |
| **Subdomain Trap** | `www.decodelabs.tech.login-update.com` | True root = rightmost domain before the path |

### The Golden Rule
```
1. PAUSE   →  Recognize the cognitive trigger (urgency, fear, authority)
2. VERIFY  →  Confirm via out-of-band channel (call a known number — not from the email)
3. REPORT  →  Don't just delete — let the security team purge it from every inbox
```

### Files
```
project-3-phishing-analyzer/
├── phishing_analyzer.py       # Main Python CLI tool
├── phishing_analyzer.html     # Interactive browser tool (AI-assisted)
└── README.md
```

---

## 🧰 Tools & Technologies

| Tool | Usage |
|------|-------|
| **Python 3** | All core project logic |
| **`re` module** | Regex pattern detection (Project 3) |
| **`string` module** | Symbol detection (Project 1) |
| **HTML / CSS / JS** | Interactive browser demos (AI-assisted) |
| **GitHub** | Version control and portfolio documentation |

---

## 📈 Skills Progression

```
Week 1 — Defensive Logic
  └── String handling · Conditional logic · Entropy · Security validation

Week 2 — Cryptography
  └── ASCII encoding · Modular arithmetic · Symmetric encryption · Vulnerability analysis

Week 3 — Threat Detection
  └── Regex · Social engineering · Triage methodology · Pattern recognition
```

---

## 🔁 Repository Structure

```
decodelabs-cybersecurity-batch2026/
│
├── README.md                          ← You are here (master overview)
│
├── project-1-password-checker/
│   ├── password_checker.py
│   ├── demo.jsx
│   └── README.md
│
├── project-2-caesar-cipher/
│   ├── cipher.py
│   ├── cipher_interactive.html
│   └── README.md
│
└── project-3-phishing-analyzer/
    ├── phishing_analyzer.py
    ├── phishing_analyzer.html
    └── README.md
```

---

## ▶️ How to Run Any Project

All projects require **Python 3.x only** — no external libraries or package installs needed.

```bash
# Project 1
python password_checker.py

# Project 2
python cipher.py

# Project 3
python phishing_analyzer.py
```

For the interactive browser demos, simply **double-click** the `.html` file — no server or setup required.

---

## 🧠 Key Takeaways Across All Projects

1. **Validation before encryption** — a weak password encrypted is still a weak password. Project 1 gates Project 2.
2. **Understanding vulnerabilities makes you a better builder** — knowing why Caesar Cipher fails explains why AES-256 exists.
3. **The strongest firewall in any organization is a trained human** — technical tools catch known patterns; human awareness catches everything else.
4. **Pythonic code matters** — using `any()` with generators over manual loops isn't just style, it's efficiency and readability at scale.
5. **Documentation is part of the work** — a project without a README is a project no one can learn from.

---



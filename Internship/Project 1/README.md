# 🔐 Password Strength Checker
> DecodeLabs Cyber Security Industrial Training | Batch 2026 | Project 1

---

## 📌 Overview

In This project, I built a **Password Strength Checker** — a Python program that evaluates any password and classifies it as **WEAK**, **MEDIUM**, or **STRONG** using a 5-point scoring system.

> *"Before you protect massive networks, you must master the fundamental principles of data validation and entropy."* — DecodeLabs Project 1 Brief

---

## 🎯 Project Goals

- Evaluate password strength based on multiple security criteria
- Classify passwords as WEAK, MEDIUM, or STRONG
- Provide actionable feedback explaining exactly what to improve
- Block commonly leaked passwords regardless of how complex they appear
- Demonstrate Pythonic coding practices throughout

---

## 🧠 The Security Logic

A password's strength is determined by two factors: **length** (entropy) and **character variety** (search space). This program evaluates both.

### Why Length Matters

A password under 8 characters is an **immediate fail** — no further checks needed. Short passwords are exponentially easier to crack via brute force because the number of possible combinations is too small.

```
6-char password (lowercase only):  26^6  =     308 million combinations
8-char password (mixed):           95^8  =   6.6 trillion combinations
12-char password (mixed):          95^12 =  540 quadrillion combinations
```

### Why Character Variety Matters

Each additional character type expands the **search space** an attacker must cover:

| Character Set Added | Search Space |
|---------------------|--------------|
| Lowercase only | 26 |
| + Uppercase | 52 |
| + Digits | 62 |
| + Symbols | ~95 (ASCII) |
| + Unicode | 143,000+ |

---

## ⚙️ How It Works

### Scoring System — 5 Points Total

| Criterion | Points | Check |
|-----------|--------|-------|
| Length ≥ 8 characters | Gate — required to proceed | `len(password) >= 8` |
| Contains uppercase letter | +1 | `any(char.isupper() for char in password)` |
| Contains digit | +1 | `any(char.isdigit() for char in password)` |
| Contains symbol | +1 | `any(char in string.punctuation for char in password)` |
| Length ≥ 12 characters | +1 (bonus) | `len(password) >= 12` |

**Note:** Length is checked first as a hard gate. Any password under 8 characters is immediately classified as WEAK with no further evaluation.

### Strength Classification

| Score | Strength |
|-------|----------|
| 0 – 2 | 🔴 WEAK |
| 3 | 🟡 MEDIUM |
| 4 – 5 | 🟢 STRONG |

---

## 💻 Core Implementation

### The Pythonic Approach

The course emphasized using `any()` with generator expressions over verbose manual loops. This is both cleaner and more efficient — `any()` short-circuits and stops scanning the moment it finds a match.

```python
# ❌ The amateur approach — verbose and slow
found = False
for i in range(len(password)):
    if password[i].isdigit():
        found = True
        break

# ✅ The Pythonic approach — clean, fast, readable
has_digit = any(char.isdigit() for char in password)
```

### Full Check Logic

```python
def check_password_strength(password: str) -> dict:
    # Gate check — length must be at least 8
    if len(password) < 8:
        return {"strength": "WEAK", "feedback": ["Too short — minimum 8 characters."]}

    # Common password check (bonus)
    if password.lower() in COMMON_PASSWORDS:
        return {"strength": "WEAK", "feedback": ["Commonly leaked password."]}

    # Pythonic pattern recognition
    has_upper  = any(char.isupper()             for char in password)
    has_digit  = any(char.isdigit()             for char in password)
    has_symbol = any(char in string.punctuation for char in password)

    # Scoring
    score = 1  # passed the length gate
    if has_upper:  score += 1
    if has_digit:  score += 1
    if has_symbol: score += 1
    if len(password) >= 12: score += 1  # bonus point

    # Classify
    strength = "WEAK" if score <= 2 else "MEDIUM" if score <= 3 else "STRONG"
    return {"score": score, "strength": strength, ...}
```

---

## ⚠️ The Common Password Blocklist (Bonus Feature)

A password can pass every technical check and still be dangerously weak if it appears in a known leaked database. For example, `Password1!` has uppercase, a digit, and a symbol — but it's one of the most commonly used passwords in the world.

The program includes a blocklist of commonly leaked passwords that are rejected immediately regardless of their technical score:

```python
COMMON_PASSWORDS = {
    "password", "123456", "password123", "qwerty", "abc123",
    "letmein", "welcome", "admin", "iloveyou", "monkey", ...
}
```

This mirrors real-world security policy — major platforms like Google and Microsoft check new passwords against breach databases before accepting them.

---

## 🔍 The Volatile Security Trap

One advanced concept covered in this project: **Data in RAM (HINNOP)**

When Python stores a password string in memory, it cannot be overwritten in place because Python strings are **immutable**. This means the password can linger in heap memory until the garbage collector clears it — a window that RAM-scraping malware (like BlackPOS) can exploit.

This is why enterprise security systems use mutable `bytearray` objects for sensitive data instead of strings, and why password managers zero out memory after use.

---

## 🗂️ Project Structure

```
project-1-password-checker/
├── password_checker.py       # Main Python CLI tool
├── Password_checker.html     # Interactive HTML demo (AI-assisted)
└── README.md                 # This file
```

---

## ▶️ How to Run

### Requirements
- Python 3.x (no external libraries needed)

```bash
python password_checker.py
```

The program will prompt you to enter a password, display the full strength report, then loop so you can test multiple passwords. Type `quit` to exit.

---

## 📋 Sample Output

```
==================================================
  🔐 PASSWORD STRENGTH REPORT — DecodeLabs
==================================================
  Password : ************
  Length   : 12 characters
  Uppercase: ✔
  Digit    : ✔
  Symbol   : ✔
  Score    : 5 / 5
--------------------------------------------------
  Result   : 🟢  STRONG
--------------------------------------------------
  Feedback:
    ✅ Excellent password! All criteria met.
==================================================
```

```
==================================================
  🔐 PASSWORD STRENGTH REPORT — DecodeLabs
==================================================
  Password : ********
  Length   : 8 characters
  Uppercase: ✘
  Digit    : ✔
  Symbol   : ✘
  Score    : 2 / 5
--------------------------------------------------
  Result   : 🔴  WEAK
--------------------------------------------------
  Feedback:
    ⚠️  Add at least one uppercase letter [A-Z].
    ⚠️  Add at least one special character [!@#$%^&*].
==================================================
```

---

## 📚 Key Concepts Learned

- Password entropy and brute force risk
- Character search space and why variety matters
- Gate-based validation logic
- Pythonic use of `any()` with generator expressions
- Common password / breach database checking
- Volatile memory (RAM) security considerations
- `string.punctuation` for symbol detection

---

## 🛡️ Built With

- **Language:** Python 3
- **Standard library:** `string`
- **Program:** DecodeLabs Cyber Security Industrial Training — Batch 2026
- **Track:** Junior Analyst / Defensive Logic

---

> *"By completing this milestone, I am confident I can build a program that evaluates risk through pure string-handling and conditional logic."*
> — DecodeLabs Project 1 Brief

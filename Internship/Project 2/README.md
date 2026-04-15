# 🔐 Caesar Cipher — Encryption & Decryption Tool
> DecodeLabs Cyber Security Industrial Training | Batch 2026 | Project 2

---

## 📌 Overview

This project implements a **Caesar Cipher** — one of the oldest and most fundamental encryption techniques in cryptography. Built as part of the DecodeLabs Cyber Security Industrial Training program, this tool demonstrates the core principles of **data confidentiality**, **symmetric encryption**, and **cryptographic vulnerability analysis**.

The Caesar Cipher works by shifting each letter in a message by a fixed number of positions in the alphabet. The same key that encrypts the message is used to decrypt it — making it a **symmetric cipher**.

---

## 🎯 Project Goals

- Implement encryption using the Caesar Cipher algorithm
- Implement decryption by reversing the shift
- Handle all edge cases (spaces, digits, punctuation, mixed case)
- Demonstrate the cipher's vulnerability via brute force
- Build an interactive CLI with a clean menu system

---

## 🧠 The Math Behind It

### Encryption Formula
```
E(x) = (x + n) % 26
```

### Decryption Formula
```
D(x) = (x - n) % 26
```

Where:
- `x` = character position in the alphabet (A=0, B=1 ... Z=25)
- `n` = shift key (chosen by the user)
- `% 26` = modular arithmetic to wrap around the alphabet

### Step-by-Step Example (encrypting 'A' with shift 3)

| Step | Operation | Result |
|------|-----------|--------|
| Input character | `'A'` | — |
| Convert to ASCII | `ord('A')` | `65` |
| Subtract base | `65 - 65` | `0` |
| Add shift key | `0 + 3` | `3` |
| Apply modulo | `3 % 26` | `3` |
| Add base back | `3 + 65` | `68` |
| Convert to character | `chr(68)` | `'D'` |

---

## 🔑 Key Python Concepts Used

| Concept | Usage |
|---------|-------|
| `ord(char)` | Converts a character to its ASCII integer |
| `chr(int)` | Converts an integer back to a character |
| `% 26` | Modular arithmetic for alphabet wrap-around |
| `char.isalpha()` | Detects letters; leaves symbols/digits unchanged |
| `char.isupper()` | Preserves original case (upper/lowercase) |
| `while True` loop | Powers the continuous CLI menu |

---

## 🗂️ Project Structure

```
cipher.py                  # Main Python script (CLI tool)
cipher_interactive.jsx     # Interactive React demo (browser-based)
README.md                  # This file
```

---

## ⚙️ How to Run

### Requirements
- Python 3.x (no external libraries needed)

### Run the CLI Tool
```bash
python cipher.py
```

### Menu Options
```
[1] Encrypt a message
[2] Decrypt a message
[3] Brute force a ciphertext
[4] Quit
```

---

## 💻 Code Walkthrough

### Encrypt Function
```python
def caesar_encrypt(plaintext: str, shift: int) -> str:
    ciphertext = []
    for char in plaintext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - base + shift) % 26 + base)
            ciphertext.append(encrypted_char)
        else:
            ciphertext.append(char)   # spaces, digits, symbols unchanged
    return ''.join(ciphertext)
```

**What's happening:**
- `char.isalpha()` — only shift letters; everything else passes through untouched
- `base` — anchors the math to either `'A'` (65) or `'a'` (97) to preserve case
- `% 26` — wraps Z back around to A (modular arithmetic)

### Decrypt Function
```python
def caesar_decrypt(ciphertext: str, shift: int) -> str:
    return caesar_encrypt(ciphertext, -shift)
```

**Elegant insight:** Decryption is just encryption with a **negative shift**. No separate logic needed — this is the beauty of symmetric ciphers.

### Brute Force Function
```python
def brute_force(ciphertext: str) -> None:
    for key in range(1, 26):
        attempt = caesar_decrypt(ciphertext, key)
        print(f"  Key {key:>2}: {attempt}")
```

**Why this works:** The Caesar Cipher only has **25 possible keys**. An attacker can try all of them in milliseconds — demonstrating why this cipher is not suitable for real-world security.

---

## 🔍 Sample Output

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

## ⚠️ Known Vulnerability: Frequency Analysis

The Caesar Cipher preserves the **statistical distribution** of letters. In English, the letter `E` appears ~12.7% of the time. Because every `E` maps to the same ciphertext letter, an attacker can:

1. Count letter frequencies in the ciphertext
2. Match the most frequent letter to `E`
3. Derive the shift key instantly

This is called **Frequency Analysis** — and it breaks Caesar Cipher without needing the key.

---

## 🚀 What Comes Next

This project is the foundation for understanding modern encryption. The evolution path:

```
Caesar Cipher  →  Vigenère Cipher  →  AES-256
(25 keys)         (polyalphabetic)    (2^256 keys)
```

Modern standards like **AES-256** use confusion, diffusion, and 128-bit keys — making brute force computationally impossible.

---

## 📚 Concepts Learned

- Symmetric encryption (same key encrypts and decrypts)
- ASCII character encoding and integer conversion
- Modular arithmetic in cryptography
- Edge case handling in string processing
- Cryptographic vulnerability: brute force and frequency analysis
- IPO model: Input → Process → Output in security systems

---

## 🛡️ Built With

- **Language:** Python 3
- **Concepts:** Caesar Cipher, ASCII encoding, modular arithmetic
- **Program:** DecodeLabs Cyber Security Industrial Training — Batch 2026
- **Track:** Junior Analyst / Defensive Logic


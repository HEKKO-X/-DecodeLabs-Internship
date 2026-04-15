# ============================================================
#  DecodeLabs | Cyber Security | Project 2
#  Basic Encryption & Decryption — Caesar Cipher
#  Batch: 2026
# ============================================================
#
#  Core Formula:
#    Encrypt: E(x) = (x + n) % 26
#    Decrypt: D(x) = (x - n) % 26
#
#  where x = character position (0-25), n = shift key
# ============================================================


def caesar_encrypt(plaintext: str, shift: int) -> str:
    """
    Encrypts plaintext using Caesar Cipher.
    - Letters (A-Z, a-z) are shifted by the key.
    - Spaces, digits, and symbols are preserved unchanged.
    - Case is preserved (uppercase stays uppercase).
    """
    ciphertext = []

    for char in plaintext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            # Subtract base → 0-25, add shift, wrap with % 26, restore base
            encrypted_char = chr((ord(char) - base + shift) % 26 + base)
            ciphertext.append(encrypted_char)
        else:
            # Spaces, punctuation, digits pass through unchanged
            ciphertext.append(char)

    return ''.join(ciphertext)


def caesar_decrypt(ciphertext: str, shift: int) -> str:
    """
    Decrypts ciphertext using Caesar Cipher.
    Decryption is just encryption with a negative shift.
    D(x) = (x - n) % 26
    """
    return caesar_encrypt(ciphertext, -shift)


def brute_force(ciphertext: str) -> None:
    """
    Bonus: tries all 25 possible shift keys.
    Useful for demonstrating the Caesar Cipher's weakness —
    only 25 possible keys = instant brute force.
    """
    print("\n  Brute force — all 25 possible decryptions:")
    print("  " + "-" * 44)
    for key in range(1, 26):
        attempt = caesar_decrypt(ciphertext, key)
        print(f"  Key {key:>2}: {attempt}")
    print()


def display_result(plaintext: str, ciphertext: str, shift: int) -> None:
    """Prints a clean encryption/decryption report."""
    print("\n" + "=" * 52)
    print("  🔐 CIPHER REPORT — DecodeLabs Project 2")
    print("=" * 52)
    print(f"  Shift key   : {shift}")
    print(f"  Plaintext   : {plaintext}")
    print(f"  Ciphertext  : {ciphertext}")
    print(f"  Decrypted   : {caesar_decrypt(ciphertext, shift)}")
    print("=" * 52)


def main():
    print("\n🛡️  DecodeLabs | Cyber Security — Project 2")
    print("    Basic Encryption & Decryption\n")

    while True:
        print("Options:")
        print("  [1] Encrypt a message")
        print("  [2] Decrypt a message")
        print("  [3] Brute force a ciphertext")
        print("  [4] Quit")
        choice = input("\nChoose an option (1-4): ").strip()

        if choice == '1':
            text  = input("  Enter plaintext  : ")
            shift = input("  Enter shift key  : ")
            if not shift.lstrip('-').isdigit():
                print("  ⚠️  Shift must be a number.\n")
                continue
            shift = int(shift) % 26
            cipher = caesar_encrypt(text, shift)
            display_result(text, cipher, shift)

        elif choice == '2':
            text  = input("  Enter ciphertext : ")
            shift = input("  Enter shift key  : ")
            if not shift.lstrip('-').isdigit():
                print("  ⚠️  Shift must be a number.\n")
                continue
            shift  = int(shift) % 26
            plain  = caesar_decrypt(text, shift)
            print("\n" + "=" * 52)
            print("  🔓 DECRYPTION RESULT")
            print("=" * 52)
            print(f"  Shift key   : {shift}")
            print(f"  Ciphertext  : {text}")
            print(f"  Plaintext   : {plain}")
            print("=" * 52 + "\n")

        elif choice == '3':
            text = input("  Enter ciphertext to brute force: ")
            brute_force(text)

        elif choice == '4':
            print("\n  Session ended. Stay secure! 🔒\n")
            break

        else:
            print("  ⚠️  Invalid option. Enter 1, 2, 3, or 4.\n")


if __name__ == "__main__":
    main()

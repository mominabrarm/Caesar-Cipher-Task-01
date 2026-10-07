"""
Caesar Cipher - Task 01
A simple Python program to encrypt and decrypt text using
the Caesar Cipher algorithm.
"""


def caesar_cipher(text, shift):
    """Shift alphabetic characters by the given amount."""
    result = []

    # Normalize large or negative shifts to the range 0-25.
    shift %= 26

    for char in text:
        if 'A' <= char <= 'Z':
            result.append(chr((ord(char) - ord('A') + shift) % 26 + ord('A')))
        elif 'a' <= char <= 'z':
            result.append(chr((ord(char) - ord('a') + shift) % 26 + ord('a')))
        else:
            # Keep spaces, numbers, and special characters unchanged.
            result.append(char)

    return ''.join(result)


def encrypt(text, shift):
    """Encrypt text using Caesar Cipher."""
    return caesar_cipher(text, shift)


def decrypt(text, shift):
    """Decrypt text using Caesar Cipher."""
    return caesar_cipher(text, -shift)


def get_shift():
    """Read and validate a numeric shift value from the user."""
    while True:
        try:
            return int(input("Enter shift value: "))
        except ValueError:
            print("Please enter a valid integer.")


def main():
    """Run the interactive Caesar Cipher menu."""
    while True:
        print("\n" + "=" * 42)
        print("           CAESAR CIPHER TOOL")
        print("=" * 42)
        print("1. Encrypt Message")
        print("2. Decrypt Message")
        print("3. Exit")
        print("=" * 42)

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            message = input("Enter message: ")
            shift = get_shift()
            print("\nEncrypted Message:", encrypt(message, shift))

        elif choice == "2":
            message = input("Enter message: ")
            shift = get_shift()
            print("\nDecrypted Message:", decrypt(message, shift))

        elif choice == "3":
            print("\nThank you for using Caesar Cipher!")
            break

        else:
            print("\nInvalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()

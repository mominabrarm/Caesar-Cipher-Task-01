# Caesar Cipher - Task 01

## 📌 Objective

Implement a Python program that can encrypt and decrypt text using the **Caesar Cipher** algorithm. The user can enter a message and a shift value.

## 🔐 What is Caesar Cipher?

Caesar Cipher is a classical substitution cipher. Each alphabetic character is shifted by a fixed number of positions in the alphabet.

For example, with a shift of `3`:

```text
A → D
B → E
C → F
...
X → A
Y → B
Z → C
```

Therefore:

```text
HELLO → KHOOR
```

Decryption reverses the shift:

```text
KHOOR → HELLO
```

## ✨ Features

- Encrypt messages
- Decrypt messages
- User-defined shift value
- Supports uppercase and lowercase letters
- Preserves spaces, numbers, and special characters
- Supports negative and large shift values
- Validates invalid shift input
- Simple interactive command-line interface

## 🛠️ Technology

- Python 3
- No external libraries required

## ▶️ How to Run

Make sure Python 3 is installed.

Open a terminal in this folder and run:

```bash
python caesar_cipher.py
```

On some systems, use:

```bash
python3 caesar_cipher.py
```

## 🧪 Example

### Encryption

```text
==========================================
           CAESAR CIPHER TOOL
==========================================
1. Encrypt Message
2. Decrypt Message
3. Exit
==========================================
Enter your choice (1-3): 1
Enter message: Hello World
Enter shift value: 3

Encrypted Message: Khoor Zruog
```

### Decryption

```text
Enter your choice (1-3): 2
Enter message: Khoor Zruog
Enter shift value: 3

Decrypted Message: Hello World
```

## 🧮 How the Algorithm Works

For an uppercase letter:

```text
Encrypted = (position + shift) mod 26
```

For decryption:

```text
Decrypted = (position - shift) mod 26
```

Python's `% 26` operation makes the alphabet wrap around from `Z` back to `A`.

## 🔒 Security Note

Caesar Cipher is intended for learning and demonstration. It is **not secure for real-world communication** because there are only 26 possible shifts and the cipher can be easily broken using brute-force analysis.

## 📁 Project Structure

```text
Caesar-Cipher-Task-01/
│
├── caesar_cipher.py
├── test_caesar_cipher.py
└── README.md
```

## 👨‍💻 Task

**Task-01: Implement Caesar Cipher**

The program demonstrates the basic concepts of encryption, decryption, substitution, and key-based transformations.

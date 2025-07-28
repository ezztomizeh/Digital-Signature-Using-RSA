# 🛡️ Digital Signature Tool (RSA + SHA-256)

This is a Python-based command-line tool for generating RSA key pairs, signing files using a private key, and verifying those signatures using the corresponding public key. It uses the `pycryptodome` library for cryptographic operations.

---

## 🔧 Features

* 🔑 Generate RSA key pairs (`1024-bit`)
* ✍️ Sign a message (text file) using a private key
* ✅ Verify a signature using a public key
* 📦 Simple command-line interface for interaction

---

## 📁 File Structure

```
digital_signature_tool/
├── main.py            # Main script with all functionality
├── private_key.pem    # Private key (generated)
├── public_key.pem     # Public key (generated)
├── signature.bin      # Signature of the message (generated)
├── message.txt        # Sample message file (user-provided)
└── README.md          # Project documentation
```

---

## 🧪 Requirements

* Python 3.6+
* [pycryptodome](https://pypi.org/project/pycryptodome/)

Install dependencies:

```bash
pip install pycryptodome
```

---

## 🚀 Usage

Run the script:

```bash
python main.py
```

You'll be prompted with the following menu:

```
[!] Welcome to digital signature generator and verifier [!]
[1] Generate Keys
[2] Sign a message
[3] Verify a message
[4] Exit
```

### 1. Generate Keys

* Generates `private_key.pem` and `public_key.pem` in the current directory.

### 2. Sign a Message

* Requires path to a text file and the private key.
* Outputs:

  * Hexadecimal hash of the message (SHA-256)
  * Signature value
  * Saves the signature to `signature.bin`

### 3. Verify a Signature

* Requires:

  * File path
  * Public key path
  * Signature (from `signature.bin` or external file)
* Outputs whether the signature is valid or invalid.

---

## 📌 Example

```bash
Enter the file path: message.txt
Enter the private key file path: private_key.pem
```

For verification:

```bash
Enter the file path: message.txt
Enter the public key file path: public_key.pem
Do you want to import external signature?(Y/n): Y
Enter the signature file path: signature.bin
```

---

## 📎 Notes

* Only text files are supported (read as string then encoded).
* Signatures are stored in binary format (`.bin`).
* RSA key size is fixed at 1024 bits for simplicity (can be increased).

---

## 🛡️ Disclaimer

This tool is for educational and demonstration purposes only. Do **not** use 1024-bit RSA in production environments—prefer 2048 bits or higher for real-world security.

---

## 👤 Author

* Developed by **Ezzudin Tomizi**
* Contributions and feedback welcome!

# Vault - Password Manager

**A secure, lightweight and fully local CLI password manager built in Python.**

![vaultgif](media/VAULT.gif)

## Features

- 🔐 **AES-GCM Encryption  with Scrypt key derivation**
- 🎲 **Unique Salt per Vault & fresh Nonce per Encryption**
- 🛡️ **Single Master Password**
- 🏠 **Fully Local -- No Cloud Storage**
- 📝 **Add Notes to Your Entries**
- 📱 **Simple CLI Interface**

## Installation

**Clone the repository**:

  ```bash
  git clone <repository-url>
  ```

  ```bash
  cd vault
  ```

**Activate a Python virtual environment**:  
(if you do not want to download dependencies system-wide)

  ```bash
  python3 -m venv .venv && source .venv/bin/activate
   ```

**Install dependencies**:

  ```bash
  pip3 install -r requirements.txt 
   ```

## Usage

### Starting the Vault

Run the main application:

```bash
python3 src/main.py
```

### First Time Setup

When you run the vault for the first time:

1. You'll be prompted to create a master password
2. A new encrypted vault file (`vault.json`) will be created in your current directory
3. **Remember your master password** - it cannot be recovered if lost!

## ⚠️ Important Notes

- **Occasionally Backup your vault file**: `vault.json`
- **Remember your master password**: There's no password recovery
- **Secure your environment**: Run on trusted systems only

## Project Structure

```
vault/
├── src/
│   ├── main.py      # Main application entry point
│   ├── vault.py     # Vault creation, loading, and saving
│   ├── crypto.py    # Encryption and decryption functions
│   └── commands.py  # In-app commands
├── media/
│   └── VAULT.gif    # Demo GIF for README
├── requirements.txt # Python dependencies
└── README.md        # This file
```

## Dependencies

packages present in requirements.txt

- **cryptography**: Provides AES-GCM encryption and Scrypt key derivation
- **cffi**: Required by cryptography for C bindings
- **pycparser**: C parser for cffi

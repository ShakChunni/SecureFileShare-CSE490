# SecureFileShare

## Description

This project demonstrates secure file storage and transmission using encryption and message authentication code (MAC) techniques. It consists of two Python scripts, `sender.py` and `receiver.py`, for encrypting and decrypting a secret file (`secret.txt`) while ensuring its integrity and authenticity.

## Files

- `sender.py`: This script encrypts `secret.txt` using AES encryption (ECB mode) and generates a MAC for integrity and authenticity verification. It saves the encrypted file as `enc.txt`, the MAC as `mac.txt`, and the encryption key as `key.txt`.

- `receiver.py`: This script decrypts `enc.txt` using the encryption key from `key.txt` and verifies the MAC from `mac.txt` to ensure the integrity and authenticity of the decrypted file, saving it as `decrypted_secret.txt`.

- `secret.txt`: This is the original secret file that you want to store securely.

- `key.txt`: This file stores the randomly generated encryption key.

- `enc.txt`: The encrypted secret file created by `sender.py`.

- `mac.txt`: The MAC generated for integrity and authenticity verification by `sender.py`.

## Usage

1. Run `sender.py` to encrypt `secret.txt` and generate the necessary files (`enc.txt`, `mac.txt`, and `key.txt`).

2. Transmit enc.txt and mac.txt securely to the receiver.

3. The receiver runs receiver.py to decrypt enc.txt and verify the MAC.

## Requirements

Python 3.x

Python packages: Crypto

## Note

Ensure that both sender and receiver have access to the same encryption key (key.txt) for successful decryption and MAC verification.

Transmit enc.txt and mac.txt through a secure channel to prevent unauthorized access and tampering.

This project is for educational purposes and may not provide the highest level of security for real-world applications. For more robust security, consider using modern encryption libraries and protocols.

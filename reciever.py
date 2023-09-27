from Crypto.Cipher import AES
from Crypto.Hash import HMAC, SHA256

# Decryption
def decrypt_file_ecb(key, input_filename, output_filename):
    cipher = AES.new(key, AES.MODE_ECB)  # Use ECB mode
    with open(input_filename, 'rb') as f:
        ciphertext = f.read()
        try:
            plaintext = cipher.decrypt(ciphertext)
            with open(output_filename, 'wb') as f:
                f.write(plaintext.rstrip(b' '))  # Remove padding
            print("Decryption successful.")
        except ValueError as e:
            print("Decryption error:", e)

# Verify MAC
def verify_mac(key, data, mac):
    h = HMAC.new(key, data, SHA256)
    return h.digest() == mac

# Read key from 'key.txt'
with open('key.txt', 'rb') as key_file:
    key = key_file.read()

input_filename = 'enc.txt'
output_filename = 'decrypted_secret.txt'
mac_filename = 'mac.txt'

decrypt_file_ecb(key, input_filename, output_filename)

received_mac = open(mac_filename, 'rb').read()
if verify_mac(key, open(input_filename, 'rb').read(), received_mac):
    print("MAC is valid. The file's integrity and authenticity are confirmed.")
else:
    print("MAC is invalid. The file may have been tampered with.")

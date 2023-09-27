from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Hash import HMAC, SHA256

# Encryption
def encrypt_file_ecb(key, input_filename, output_filename):
    cipher = AES.new(key, AES.MODE_ECB)  # Use ECB mode
    with open(input_filename, 'rb') as f:
        plaintext = f.read()
        # Pad the plaintext to be a multiple of block size (16 bytes)
        while len(plaintext) % 16 != 0:
            plaintext += b' '
        ciphertext = cipher.encrypt(plaintext)
    with open(output_filename, 'wb') as f:
        f.write(ciphertext)

# Generate MAC
def generate_mac(key, data):
    h = HMAC.new(key, data, SHA256)
    return h.digest()

# Generate random key
key = get_random_bytes(16)  # 16 bytes = 128 bits

input_filename = 'secret.txt'
output_filename = 'enc.txt'

encrypt_file_ecb(key, input_filename, output_filename)

mac = generate_mac(key, open(output_filename, 'rb').read())
with open('mac.txt', 'wb') as mac_file:
    mac_file.write(mac)

# Save key to 'key.txt'
with open('key.txt', 'wb') as key_file:
    key_file.write(key)
    

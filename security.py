from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import os

# Generate a 256-bit (32-byte) key
key = get_random_bytes(32)

# AES-256 in CBC mode (requires an Initialization Vector, IV)
iv = get_random_bytes(16)  # IV must be 16 bytes for AES

def encrypt_image(input_path, output_path):
    # Read image as binary
    with open(input_path, 'rb') as f:
        image_data = f.read()
    
    # Pad data to be AES-block-aligned
    padded_data = pad(image_data, AES.block_size)
    
    # Encrypt
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted_data = cipher.encrypt(padded_data)
    
    # Save encrypted data (IV + ciphertext)
    with open(output_path, 'wb') as f:
        f.write(iv + encrypted_data)

def decrypt_image(input_path, output_path):
    # Read encrypted file
    with open(input_path, 'rb') as f:
        encrypted_data = f.read()
    
    # Extract IV (first 16 bytes)
    iv = encrypted_data[:16]
    ciphertext = encrypted_data[16:]
    
    # Decrypt
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = unpad(cipher.decrypt(ciphertext), AES.block_size)
    
    # Save decrypted image
    with open(output_path, 'wb') as f:
        f.write(decrypted_data)

# Example usage
input_image = "pelvic_scan.png"
encrypted_image = "encrypted_pelvic.bin"
decrypted_image = "decrypted_pelvic.png"

# Encrypt
encrypt_image(input_image, encrypted_image)
print("Image encrypted!")

# Decrypt
decrypt_image(encrypted_image, decrypted_image)
print("Image decrypted!")
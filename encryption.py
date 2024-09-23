# encrypt.py

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import binascii

def get_cipher(key, mode, iv=None):
    if mode == 'ECB':
        return AES.new(key, AES.MODE_ECB)
    elif mode == 'CBC':
        return AES.new(key, AES.MODE_CBC, iv)
    elif mode == 'CFB':
        return AES.new(key, AES.MODE_CFB, iv)
    elif mode == 'OFB':
        return AES.new(key, AES.MODE_OFB, iv)
    else:
        raise ValueError("Unsupported mode of operation")

def encrypt(data, key, mode, iv=None):
    # Generate IV if needed and not provided
    if iv is None and mode in ['CBC', 'CFB', 'OFB']:
        iv = get_random_bytes(AES.block_size)
        print(f"Generated IV: {iv.hex()}")

    # Create cipher object
    cipher = get_cipher(key, mode, iv)

    # Apply padding automatically for ECB/CBC modes
    if mode in ['ECB', 'CBC']:
        data = pad(data.encode(), AES.block_size)
    else:
        # For CFB and OFB modes, convert data to bytes directly without padding
        data = data.encode()
    
    # Encrypt data
    encrypted_data = cipher.encrypt(data)
    return iv, encrypted_data

def main():
    # User inputs
    data = input("Enter data to encrypt: ")
    key_size = int(input("Enter key size (128, 192, 256): "))
    mode = input("Enter mode of operation (ECB, CBC, CFB, OFB): ")
    
    # Key input
    key_choice = input("Do you want to enter a custom key? (yes/no): ").strip().lower()
    if key_choice == 'yes':
        key_input = input(f"Enter the key (must be {key_size // 8} characters long): ")
        if len(key_input) != key_size // 8:
            print(f"Error: Key must be {key_size // 8} characters long!")
            return
        key = key_input.encode()
    else:
        key = get_random_bytes(key_size // 8)
        print(f"Generated Key: {key.hex()}")

    # IV input (if applicable)
    iv = None
    if mode in ['CBC', 'CFB', 'OFB']:
        iv_choice = input("Do you want to enter a custom IV? (yes/no): ").strip().lower()
        if iv_choice == 'yes':
            iv_input = input(f"Enter the IV (must be {AES.block_size} characters long): ")
            if len(iv_input) != AES.block_size:
                print(f"Error: IV must be {AES.block_size} characters long!")
                return
            iv = iv_input.encode()
        else:
            iv = get_random_bytes(AES.block_size)
            print(f"Generated IV: {iv.hex()}")

    # Encrypt
    try:
        iv, encrypted_data = encrypt(data, key, mode, iv)
        print(f"Encrypted Data: {encrypted_data.hex().upper()}")  # Convert to uppercase
    except ValueError as e:
        print(f"Encryption Error: {e}")
        return

    # Display key, IV, and encrypted data for use in decryption
    print(f"Key: {key.hex()}")
    if iv is not None:
        print(f"IV: {iv.hex()}")

if __name__ == "__main__":
    main()

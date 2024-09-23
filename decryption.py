# decrypt.py

from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
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

def decrypt(encrypted_data, key, mode, iv=None):
    # Create cipher object
    cipher = get_cipher(key, mode, iv)

    # Decrypt data
    decrypted_data = cipher.decrypt(encrypted_data)
    
    # Remove padding if required for ECB/CBC
    if mode in ['ECB', 'CBC']:
        decrypted_data = unpad(decrypted_data, AES.block_size)
    
    return decrypted_data

def main():
    # User inputs
    encrypted_hex = input("Enter encrypted data (hex): ")
    encrypted_data = binascii.unhexlify(encrypted_hex)
    
    key_size = int(input("Enter key size (128, 192, 256): "))
    mode = input("Enter mode of operation (ECB, CBC, CFB, OFB): ")
    
    # Key input format
    key_format = input("Do you want to enter the key as hex or text? (hex/text): ").strip().lower()
    
    if key_format == 'hex':
        key_input = input(f"Enter the key in hex (must be {2 * (key_size // 8)} hex characters long): ")
        if len(key_input) != 2 * (key_size // 8):
            print(f"Error: Key must be {2 * (key_size // 8)} hex characters long!")
            return
        key = binascii.unhexlify(key_input)
    elif key_format == 'text':
        key_input = input(f"Enter the key in text (must be {key_size // 8} characters long): ")
        if len(key_input) != key_size // 8:
            print(f"Error: Key must be {key_size // 8} characters long!")
            return
        key = key_input.encode()
    else:
        print("Invalid option! Please enter 'hex' or 'text'.")
        return

    # IV input (if applicable)
    iv = None
    if mode in ['CBC', 'CFB', 'OFB']:
        iv_format = input("Do you want to enter the IV as hex or text? (hex/text): ").strip().lower()
        
        if iv_format == 'hex':
            iv_input = input(f"Enter the IV in hex (must be {2 * AES.block_size} hex characters long): ")
            if len(iv_input) != 2 * AES.block_size:  # Expecting hex representation, hence 2*block_size
                print(f"Error: IV must be {2 * AES.block_size} hex characters long!")
                return
            iv = binascii.unhexlify(iv_input)
        elif iv_format == 'text':
            iv_input = input(f"Enter the IV in text (must be {AES.block_size} characters long): ")
            if len(iv_input) != AES.block_size:
                print(f"Error: IV must be {AES.block_size} characters long!")
                return
            iv = iv_input.encode()
        else:
            print("Invalid option! Please enter 'hex' or 'text'.")
            return

    # Decrypt
    try:
        decrypted_data = decrypt(encrypted_data, key, mode, iv)
        print(f"Decrypted Data: {decrypted_data.decode()}")
    except (ValueError, KeyError) as e:
        print(f"Decryption Error: {e}")

if __name__ == "__main__":
    main()

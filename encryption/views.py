import binascii
from django.shortcuts import render
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

# Helper function to get AES cipher based on mode and IV
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
        raise ValueError('Invalid mode')

# Helper function to generate a random key
def generate_random_key(key_size):
    return get_random_bytes(key_size // 8)

# Helper function to generate a random IV
def generate_random_iv():
    return get_random_bytes(AES.block_size)

def encryption_decryption_view(request):
    encrypt_result = None
    decrypt_result = None
    generated_key = None
    generated_iv = None
    result_message = None  # Message to be displayed in case of validation errors

    if request.method == 'POST':
        action = request.POST.get('action')
        key_size = int(request.POST.get('key_size'))
        mode = request.POST.get('mode')
        key_input = request.POST.get('key_input')
        iv_input = request.POST.get('iv_input')
        key_format = request.POST.get('key_format')  # For decryption only
        iv_format = request.POST.get('iv_format')    # For decryption only

        # Encryption logic
        if action == 'encrypt':
            if key_input:
                if len(key_input) != key_size // 8:
                    result_message = f'Custom key must be {key_size // 8} characters long!'
                    return render(request, 'encrypt_decrypt.html', {'result_message': result_message})
                key = key_input.encode('utf-8')
            else:
                key = generate_random_key(key_size)
                generated_key = binascii.hexlify(key).decode()

            if iv_input and mode != 'ECB':
                if len(iv_input) != AES.block_size:
                    result_message = f'Custom IV must be {AES.block_size} characters long!'
                    return render(request, 'encrypt_decrypt.html', {'result_message': result_message})
                iv = iv_input.encode('utf-8')
            else:
                iv = generate_random_iv() if mode != 'ECB' else None
                if iv:
                    generated_iv = binascii.hexlify(iv).decode()

            # Encrypt data
            data = request.POST.get('data')
            cipher = get_cipher(key, mode, iv)
            encrypted_data = cipher.encrypt(pad(data.encode(), AES.block_size))
            encrypt_result = binascii.hexlify(encrypted_data).decode().upper()

        # Decryption logic
        elif action == 'decrypt':
            encrypted_data = request.POST.get('encrypted_data')

            # Key validation
            if key_format == 'hex':
                try:
                    if len(key_input) != (key_size // 8) * 2:
                        result_message = f'Hex key must be {(key_size // 8) * 2} characters long!'
                        return render(request, 'encrypt_decrypt.html', {'result_message': result_message})
                    key = binascii.unhexlify(key_input)
                except binascii.Error:
                    result_message = 'Invalid hex key format!'
                    return render(request, 'encrypt_decrypt.html', {'result_message': result_message})
            else:
                if len(key_input) != key_size // 8:
                    result_message = f'Custom key must be {key_size // 8} characters long!'
                    return render(request, 'encrypt_decrypt.html', {'result_message': result_message})
                key = key_input.encode('utf-8')

            # IV validation
            if mode != 'ECB':
                if iv_input:
                    try:
                        if iv_format == 'hex':
                            if len(iv_input) != 32:
                                result_message = 'Hex IV must be 32 characters long!'
                                return render(request, 'encrypt_decrypt.html', {'result_message': result_message})
                            iv = binascii.unhexlify(iv_input)
                        elif iv_format == 'text':
                            if len(iv_input) != 16:
                                result_message = 'Custom IV must be 16 characters long!'
                                return render(request, 'encrypt_decrypt.html', {'result_message': result_message})
                            iv = iv_input.encode('utf-8')
                        else:
                            result_message = 'Invalid IV format selected!'
                            return render(request, 'encrypt_decrypt.html', {'result_message': result_message})
                    except binascii.Error:
                        result_message = 'Invalid hex IV format!'
                        return render(request, 'encrypt_decrypt.html', {'result_message': result_message})
                else:
                    result_message = 'IV is required for decryption in this mode!'
                    return render(request, 'encrypt_decrypt.html', {'result_message': result_message})
            else:
                iv = None

            # Decrypt data
            try:
                cipher = get_cipher(key, mode, iv)
                decrypted_data = unpad(cipher.decrypt(binascii.unhexlify(encrypted_data)), AES.block_size)
                decrypt_result = decrypted_data.decode('utf-8')
            except (ValueError, KeyError):
                decrypt_result = 'Decryption Error: Incorrect padding or invalid key/IV.'


    return render(request, 'encrypt_decrypt.html', {
        'encrypt_result': encrypt_result,
        'decrypt_result': decrypt_result,
        'generated_key': generated_key,
        'generated_iv': generated_iv,
        'result_message': result_message,
    })

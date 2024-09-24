# Advanced Encryption Standard AES Tool

## Provides secure data protection by converting readable information into an unreadable format. 

### Authors: Rein Mark Del Rosario & Jose Vyncent Ramos 
### Date: Last Edited Sept 24, 2024
### Version: 1.0 

## System Requirements: 

### Hardware:
#### CPU: Dual-core processor (e.g., Intel Core i3 or equivalent)
#### RAM: 4 GB
#### Storage: 10 GB of free space (for the OS, Django, and dependencies)

### Software:
#### Operating System: Any modern OS (Windows, macOS, Linux)
#### Python: Version 3.6 or later
#### Django: Version 2.x or later
#### Libraries: pycryptodome for encryption functionality


# Functional Description:

Input: Expected data formats and sources.


Processing:
 
AES Encryption Process:
The user provides the plaintext (the data to be encrypted), the encryption key, the mode of operation (like ECB or CBC), and an optional initialization vector (IV).
The encryption key must be of a specific length (128, 192, or 256 bits). If using modes that require an IV (like CBC), generate a random IV or use a user-provided one.
An AES cipher object is created using the key and the specified mode. The mode determines how blocks of data are processed (e.g., whether the same key can encrypt multiple blocks independently).
If using block modes (like ECB or CBC), the plaintext is padded to ensure its length is a multiple of the AES block size (16 bytes). This prevents issues during encryption.
The padded plaintext is processed in blocks. Each block is transformed using the AES algorithm, which involves several rounds of substitution and permutation operations based on the key. The final output is ciphertext, which appears random and unreadable.

AES Decryption Process:
The user provides the ciphertext, the same key used for encryption, and the IV if required by the mode.
A new AES cipher object is created using the same key and IV (if applicable).
The ciphertext is processed in blocks. The AES algorithm reverses the encryption operations, transforming the ciphertext back into padded plaintext.
After decryption, the plaintext may still be padded. The padding is removed to retrieve the original data.
The result is the original plaintext, now restored from the ciphertext.

Output: Generated data, formats, and destinations.


# Security Considerations

Vulnerability Assessment: 
Using weak or easily guessable keys (e.g., short keys or common phrases).
Poor handling of keys, such as hardcoding them in the source code or storing them insecurely.
 Reusing the same IV with the same key in modes like CBC can lead to predictable patterns in ciphertext.
Without proper authentication, an attacker could modify the ciphertext without detection.
Sending sensitive data over insecure channels (e.g., HTTP instead of HTTPS) exposes it to interception.

Mitigation Strategies:
Ensure keys are generated using a secure random number generator and are of appropriate length (128, 192, or 256 bits).
Use secure key management practices, such as environment variables, secure vaults, or hardware security modules (HSMs).
 Always generate a new, random IV for each encryption operation and ensure it is unique.
Implement message authentication codes (MACs) or use authenticated encryption schemes.
Always use secure transport protocols like TLS to encrypt data in transit.

Testing: 
Key Rotation: Implement regular key rotation and verify that old keys are securely retired.
Code Review: Conduct thorough code reviews focusing on cryptographic implementations, looking for hardcoded keys, improper IV handling, or insecure practices.
Functional Testing: Verify that the encryption and decryption processes function correctly, consistently producing the expected output.
Boundary Testing : Test with edge cases, such as maximum and minimum input sizes, to ensure robustness.
Penetration Testing: Conduct regular penetration testing to assess the security posture and identify possible attack vectors.


# Usage Instructions

### Prerequisites:
- At least Python v3.6 (or higher)


### Run cmd and enter the following commands: 

#### Install pycryptodome
```
pip install pycryptodome
```

#### Install Django
```
pip install django
```


#### Navigate to directory:
```
cd aes_project
```

#### Run the server:
```
python manage.py runserver
```

# Error Handling

Error Codes: A list of possible errors and their meanings.
ModuleNotFoundError - Indicates that a required module or package (e.g., Crypto) is not installed or cannot be found.
ValueError - Raised when an invalid value is encountered, such as an unsupported encryption mode or incorrect key size.
KeyError - Occurs when trying to access a dictionary key that does not exist, often related to settings or configuration.
InvalidKeyException - Raised when the provided key length is not valid (must be 16, 24, or 32 bytes).
InvalidIVException - Occurs when the initialization vector (IV) provided is of incorrect length or format.
EncryptionError - A general error that occurs during the encryption process, indicating that something went wrong.
DecryptionError - Similar to EncryptionError, but indicates an issue during the decryption process.
Http404 - Raised when a requested URL is not found in the Django application.

# Recovery Procedures:
Install the necessary package using pip install pycryptodome.
Ensure that the mode and key size provided are valid and supported by the AES implementation.
Verify that all required keys in your configurations or data structures are present.
 Use a key of the appropriate length according to AES specifications.
 Ensure that the IV is the correct length (16 bytes for AES) and properly formatted.
Review the error message for specifics and check inputs, keys, and configuration.
 Check that the ciphertext and keys are valid and that the correct decryption mode is being used.
Ensure that the URL patterns are correctly configured and that the views are properly defined.


# Maintenance Log

Date: Sept 21, 2024

Changes: Project start

Author: Rein Mark Del Rosario


Date: Sept 21, 2024

Changes: Implement initial AES encrypt/decrypt script

Author: Rein Mark Del Rosario


Date: Sept 23, 2024

Changes: Implement Django Web Framework to build web page

Author: Rein Mark Del Rosario


Date: Sept 24, 2024

Changes: Add CSS stylesheet

Author: Jose Vyncent Ramos

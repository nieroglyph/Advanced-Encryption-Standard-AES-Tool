# Advanced Encryption Standard AES Tool

## This project implements AES encryption and decryption with multiple modes (ECB, CBC, CFB, OFB) in a Django web application.

### Authors: Rein Mark Del Rosario & Jose Vyncent Ramos 
### Date: Last Edited Sept 24, 2024
### Version: 1.0 
### Purpose: To provide a user-friendly web interface for encryption and decryption of data using AES encryption with various operations (ECB, CBC, CFB, OFB). The project aims to demonstrate the principles of the algorithm while ensuring data security and handling potential errors in the process.

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


## Functional Description:

### Input: Expected Data Formats and Sources
- Plaintext Message: The user provides a message to be encrypted. This can be any string of text.
- Ciphertext: The encrypted message, input by the user during decryption.
- Key: The key used for AES encryption/decryption. It can be provided in either text or hexadecimal format.
  - Text format: Must match the key size (16 characters for 128-bit, 24 for 192-bit, or 32 for 256-bit).
  - Hex format: Must be twice the key size in characters (32 characters for 128-bit, 48 for 192-bit, 64 for 256-bit).
- Initialization Vector (IV): The IV can be input in either text or hex format.
  - Text format: 16 characters long.
  - Hex format: 32 characters long.
- Key Size: Users choose the key size from options 128, 192, or 256 bits.
- IV Format: Users specify whether the IV is in text or hex format.
- Key Format: Users specify whether the key is in text or hex format.

### Processing: A Step-by-Step Explanation of the Program's Logic
#### Encryption:

The user can select from four modes of operation: Electronic Code Book (ECB), Cipher Block Chaining (CBC), 
Cipher FeedBack mode (CFB), Output FeedBack (OFB). The user then inputs the plaintext message, key, 
and IV (or lets the system generate random ones). The script validates the key and IV based on 
the user-specified format (text or hex) and key size. If the input passes validation, the message 
is encrypted using the AES algorithm in different modes. The system generates the ciphertext as the output.

#### Decyption:

The user inputs the ciphertext, key, and IV.
The system validates the key and IV formats.
If valid, the system decrypts the ciphertext using the AES algorithm and returns the original plaintext.

#### Validation:

For keys and IVs in hex format, the system verifies that the input is a valid hex string of the correct length.
For text format, the system ensures the input matches the correct length (based on the key size and IV).

### Output: Generated Data, Formats, and Destinations

Encryption Output: Ciphertext generated from the plaintext message using AES encryption. This ciphertext is displayed to the user.


Decryption Output: The original plaintext generated from the provided ciphertext, key, and IV during the decryption process.


## Security Considerations
#### Vulnerability Assessment: Risks include weak keys, predictable IVs, or insecure modes like ECB.
#### Mitigation Strategies: Enforce strong key/IV generation, limit ECB usage, and validate input lengths.
#### Testing: Regular checks to ensure keys and encryption are secure, with input validation to prevent incorrect formats.


## Usage Instructions

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

## Error Handling
#### Error Codes: Alerts for invalid key/IV formats, incorrect lengths, and decryption failures.
#### Recovery Procedures: Guide users to correct key/IV input and retry operations after errors.


## Maintenance Log

Date: Sept 21, 2024 </br>
Changes: Project start </br>
Author: Rein Mark Del Rosario </br>
</br>
Date: Sept 21, 2024 </br>
Changes: Implement initial AES encrypt/decrypt script </br>
Author: Rein Mark Del Rosario </br>
</br>
Date: Sept 23, 2024 </br>
Changes: Implement Django Web Framework to build web page </br>
Author: Rein Mark Del Rosario </br>
</br>
Date: Sept 24, 2024 </br>
Changes: Add CSS stylesheet </br>
Author: Jose Vyncent Ramos </br>

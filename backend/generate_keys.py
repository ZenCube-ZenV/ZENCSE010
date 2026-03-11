"""
ECDSA P-256 Key Pair Generator — US-04

Run this ONCE before starting the application:
    python generate_keys.py

TODO (Students):
  Implement the key generation logic:

  1. Create the keys/ directory if it doesn't exist (os.makedirs)

  2. If private_key.pem already exists, ask for confirmation before overwriting
     (overwriting invalidates all previously signed certificates)

  3. Generate an ECDSA P-256 private key:
       from cryptography.hazmat.primitives.asymmetric import ec
       private_key = ec.generate_private_key(ec.SECP256R1())

  4. Derive the public key:
       public_key = private_key.public_key()

  5. Save private_key.pem to keys/ in PEM + PKCS8 format (NoEncryption)
     Hint:
       from cryptography.hazmat.primitives import serialization
       private_key.private_bytes(
           encoding=serialization.Encoding.PEM,
           format=serialization.PrivateFormat.PKCS8,
           encryption_algorithm=serialization.NoEncryption(),
       )

  6. Save public_key.pem to keys/ in PEM + SubjectPublicKeyInfo format

  7. Print confirmation messages

  Note: keys/private_key.pem is already in .gitignore — never commit it.
"""

# TODO: implement key generation here

import os
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization

# create keys directory if it does not exist
os.makedirs("keys", exist_ok=True)

private_key_path = "keys/private_key.pem"
public_key_path = "keys/public_key.pem"

# check if private key already exists
if os.path.exists(private_key_path):
    confirm = input("Private key already exists. Overwrite? (y/n): ")
    if confirm.lower() != "y":
        print("Key generation cancelled.")
        exit()

# generate private key
private_key = ec.generate_private_key(ec.SECP256R1())

# derive public key
public_key = private_key.public_key()

# save private key
with open(private_key_path, "wb") as f:
    f.write(
        private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption(),
        )
    )

# save public key
with open(public_key_path, "wb") as f:
    f.write(
        public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo,
        )
    )

print("✅ ECDSA key pair generated successfully!")
print("Private key:", private_key_path)
print("Public key:", public_key_path)

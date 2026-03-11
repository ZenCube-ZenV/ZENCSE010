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
import sys
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization

def generate_keys():
    """
    Utility that creates an ECDSA P-256 key pair.
    """
    keys_dir = "keys"
    private_key_path = os.path.join(keys_dir, "private_key.pem")
    public_key_path = os.path.join(keys_dir, "public_key.pem")

    # 1. Create the keys/ directory if it doesn't exist
    if not os.path.exists(keys_dir):
        os.makedirs(keys_dir)

    # 2. If private_key.pem already exists, ask for confirmation before overwriting
    if os.path.exists(private_key_path):
        ans = input("Private key already exists. Overwriting invalidates all previously signed certificates. Continue? [y/N]: ")
        if ans.lower() not in ("y", "yes"):
            print("Aborted.")
            sys.exit(0)

    # 3. Generate an ECDSA P-256 private key
    print("Generating ECDSA P-256 private key...")
    private_key = ec.generate_private_key(ec.SECP256R1())

    # 4. Derive the public key
    print("Deriving public key...")
    public_key = private_key.public_key()

    # 5. Save private_key.pem to keys/ in PEM + PKCS8 format (NoEncryption)
    with open(private_key_path, "wb") as f:
        f.write(
            private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.NoEncryption(),
            )
        )
    
    # 6. Save public_key.pem to keys/ in PEM + SubjectPublicKeyInfo format
    with open(public_key_path, "wb") as f:
        f.write(
            public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo,
            )
        )

    # 7. Print confirmation messages
    print(f"Success! Keys saved to directory: {keys_dir}/")
    print(f" - {private_key_path}")
    print(f" - {public_key_path}")

if __name__ == "__main__":
    generate_keys()

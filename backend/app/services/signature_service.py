"""
ECDSA P-256 Digital Signature Service.

TODO (Students):
  Implement two functions:

  1. sign_certificate(data: dict) -> tuple[str, str]
     - Canonicalize the dict: sort keys, convert to JSON string
     - Compute SHA-256 hash of the canonical string
     - Load private key from settings.private_key_path (PEM format)
     - Sign the hash using ECDSA with SHA-256 (from `cryptography` library)
     - Return (base64-encoded signature, hex data_hash)

     Hint:
       from cryptography.hazmat.primitives.asymmetric import ec
       from cryptography.hazmat.primitives import hashes, serialization
       private_key.sign(data_bytes, ec.ECDSA(hashes.SHA256()))

  2. verify_certificate(data: dict, signature_b64: str) -> bool
     - Canonicalize + hash the data the same way as sign_certificate
     - Load public key from settings.public_key_path
     - Decode the base64 signature
     - Verify using the public key
     - Return True if valid, False if verification fails

     Hint: Use try/except around public_key.verify(...)
           It raises InvalidSignature if verification fails.

  Also provide:
  3. generate_keys() — a utility to generate a new ECDSA P-256 key pair
     and save private_key.pem + public_key.pem to the keys/ folder.
     Run this ONCE to set up the system.
"""

# TODO: implement SignatureService here
import json
import base64
import binascii
from typing import Tuple

from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.exceptions import InvalidSignature

# Assuming settings is defined somewhere in the app, for now we will mock it
# You might need to adjust this import based on your actual project structure
class Settings:
    private_key_path = "keys/private_key.pem"
    public_key_path = "keys/public_key.pem"

settings = Settings()

def sign_certificate(data: dict) -> Tuple[str, str]:
    """
    Signs certificate data with ECDSA P-256.
    Returns (base64_signature, hex data_hash)
    """
    # 1. Canonicalize the dict: sort keys, convert to JSON string
    canonical_data = json.dumps(data, sort_keys=True, separators=(',', ':'))
    
    # 2. Compute SHA-256 hash of the canonical string
    digest = hashes.Hash(hashes.SHA256())
    digest.update(canonical_data.encode('utf-8'))
    data_hash_bytes = digest.finalize()
    
    # Return hex data hash prefixed with "sha256:"
    data_hash_hex = f"sha256:{binascii.hexlify(data_hash_bytes).decode('utf-8')}"
    
    # 3. Load private key from settings.private_key_path
    with open(settings.private_key_path, "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
        )
    
    # 4. Sign the hash using ECDSA with SHA 256
    signature = private_key.sign(
        canonical_data.encode('utf-8'),
        ec.ECDSA(hashes.SHA256())
    )
    
    # 5. Return base64-encoded signature
    base64_signature = base64.b64encode(signature).decode('utf-8')
    
    return base64_signature, data_hash_hex


def verify_certificate(data: dict, signature_b64: str) -> bool:
    """
    Verifies a certificate's ECDSA P-256 signature.
    """
    # 1. Canonicalize & hash the data the same way as sign_certificate
    canonical_data = json.dumps(data, sort_keys=True, separators=(',', ':'))
    
    # 2. Load public key from settings.public_key_path
    with open(settings.public_key_path, "rb") as key_file:
        public_key = serialization.load_pem_public_key(
            key_file.read()
        )
    
    # 3. Decode the base64 signature
    try:
        signature = base64.b64decode(signature_b64)
    except (binascii.Error, ValueError):
        return False
        
    # 4. Verify using the public key
    try:
        public_key.verify(
            signature,
            canonical_data.encode('utf-8'),
            ec.ECDSA(hashes.SHA256())
        )
        # 5. Return True if valid
        return True
    except InvalidSignature:
        # Return False if verification fails
        return False

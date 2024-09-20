from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
import os
import time


class RSAKeyManager:
    def __init__(self, key_size=2048):
        self.key_size = key_size
        self.keys = {}
        self.logs = []

    def generate_keys(self, facility_id):
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=self.key_size,
            backend=default_backend()
        )
        public_key = private_key.public_key()

        self.keys[facility_id] = {
            "public_key": public_key,
            "private_key": private_key
        }
        self.log(f"Keys generated for {facility_id}.")
        return public_key

    def distribute_keys(self, facility_id):
        keys = self.keys.get(facility_id)
        if keys:
            self.log(f"Keys distributed to {facility_id}.")
            return keys["public_key"], keys["private_key"]
        self.log(f"Keys not found for {facility_id}.")
        return None

    def log(self, message):
        entry = f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {message}"
        self.logs.append(entry)
        print(entry)

    def encrypt(self, public_key, message):
        ciphertext = public_key.encrypt(
            message.encode("utf-8"),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return ciphertext

    def decrypt(self, private_key, ciphertext):
        plaintext = private_key.decrypt(
            ciphertext,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return plaintext.decode("utf-8")


# Example Usage
km = RSAKeyManager()
facility_id = "hospital1"

# Key Generation and Distribution
public_key = km.generate_keys(facility_id)
public_key, private_key = km.distribute_keys(facility_id)

# Encrypt and Decrypt Example
message = "datadatadatadatadata"
ciphertext = km.encrypt(public_key, message)
print(f"Encrypted: {ciphertext}")

# Decrypt the message
decrypted_message = km.decrypt(private_key, ciphertext)
print(f"Decrypted: {decrypted_message}")

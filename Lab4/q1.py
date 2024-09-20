from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.hashes import Hash, SHA256
import os
import time

class DRMSystem:
    def __init__(self, key_size=2048):
        self.key_size = key_size
        self.master_key_pair = None
        self.content_keys = {}
        self.access_control = {}
        self.logs = []

    def generate_master_key(self):
        parameters = dh.generate_parameters(generator=2, key_size=self.key_size, backend=default_backend())
        self.master_key_pair = parameters.generate_private_key()
        self.log("Master key pair generated.")

    def encrypt_content(self, content_id, content):
        # Create a SHA256 hash object
        hash_object = Hash(SHA256(), backend=default_backend())
        hash_object.update(content)
        h = hash_object.finalize()  # Finalize to get the digest

        # Placeholder for the actual encrypted content
        self.content_keys[content_id] = h
        self.log(f"Content {content_id} encrypted.")

    def distribute_key(self, customer_id, content_id):
        self.access_control[(customer_id, content_id)] = time.time() + 3600
        self.log(f"Access granted to {customer_id} for content {content_id}.")

    def revoke_access(self, customer_id, content_id):
        if (customer_id, content_id) in self.access_control:
            del self.access_control[(customer_id, content_id)]
            self.log(f"Access revoked for {customer_id} for content {content_id}.")

    def key_revocation(self):
        self.generate_master_key()
        self.log("Master key revoked and renewed.")

    def check_access(self, customer_id, content_id):
        if (customer_id, content_id) in self.access_control:
            access_time = self.access_control[(customer_id, content_id)]
            if time.time() <= access_time:
                return True
        return False

    def secure_store_key(self):
        pem = self.master_key_pair.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL)
        with open("private_key.pem", "wb") as f:
            f.write(pem)
        os.chmod("private_key.pem", 0o600)
        self.log("Master private key securely stored.")

    def log(self, message):
        self.logs.append(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {message}")
        print(message)

# Example Usage
if __name__ == "__main__":
    drm = DRMSystem()
    drm.generate_master_key()
    drm.encrypt_content("content1", b"Some digital content")
    drm.distribute_key("customer1", "content1")
    drm.revoke_access("customer1", "content1")
    drm.key_revocation()
    drm.secure_store_key()

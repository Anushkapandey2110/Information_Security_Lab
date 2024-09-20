from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os
import random

random.seed(42)


def fixed_rng(seed, length):
    random.seed(seed)
    return os.urandom(length)


# Generate ECC private and public keys
private_key = ec.generate_private_key(ec.SECP256R1(), default_backend())
public_key = private_key.public_key()


def encrypt_message(public_key, message):
    # Generate ephemeral key pair
    ephemeral_private_key = ec.generate_private_key(ec.SECP256R1(), default_backend())
    ephemeral_public_key = ephemeral_private_key.public_key()

    # Compute shared secret
    shared_secret = ephemeral_private_key.exchange(ec.ECDH(), public_key)

    # Derive key using HKDF
    derived_key = HKDF(
        algorithm=hashes.SHA256(),
        length=32,
        salt=None,
        info=b'',
        backend=default_backend()
    ).derive(shared_secret)

    iv = fixed_rng(999, 16)
    cipher = Cipher(algorithms.AES(derived_key), modes.GCM(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    ciphertext = encryptor.update(message) + encryptor.finalize()
    tag = encryptor.tag
    return ephemeral_public_key, iv, ciphertext, tag


def decrypt_message(private_key, ephemeral_public_key, iv, ciphertext, tag):
    # Compute shared secret
    shared_secret = private_key.exchange(ec.ECDH(), ephemeral_public_key)

    # Derive key using HKDF
    derived_key = HKDF(
        algorithm=hashes.SHA256(),
        length=32,
        salt=None,
        info=b'',
        backend=default_backend()
    ).derive(shared_secret)

    cipher = Cipher(algorithms.AES(derived_key), modes.GCM(iv, tag), backend=default_backend())
    decryptor = cipher.decryptor()

    decrypted_message = decryptor.update(ciphertext) + decryptor.finalize()
    return decrypted_message


message = b"Secure Transactions"
ephemeral_public_key, iv, ciphertext, tag = encrypt_message(public_key, message)
print("Ciphertext (in hex):", ciphertext.hex())

decrypted_message = decrypt_message(private_key, ephemeral_public_key, iv, ciphertext, tag)
print("Decrypted message:", decrypted_message.decode())
_key, message)
print("Ciphertext (in hex):", ciphertext.hex())

decrypted_message = decrypt_message(private_key, ephemeral_public_key, iv, ciphertext, tag)
print("Decrypted message:", decrypted_message.decode())

from os import error
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

while True:
    filename = input("Filename: ")
    
    try:
        f = open(filename, 'rb')
        message = f.read()
        f.close()
    except:
        print(error)



    with open("public_key.pem", "rb") as key_file:
        public_key = serialization.load_pem_public_key(
            key_file.read(),
            backend=default_backend()
        )

    encrypted = public_key.encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    f = open(filename + '.encrypted', 'wb')
    f.write(encrypted)
    f.close()
    
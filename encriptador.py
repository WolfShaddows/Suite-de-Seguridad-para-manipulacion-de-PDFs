# encriptador.py
from cryptography.fernet import Fernet

class Encriptador:
    @staticmethod
    def encriptar(mensaje):
        clave_secreta = Fernet.generate_key()
        cipher_suite = Fernet(clave_secreta)
        mensaje_encriptado = cipher_suite.encrypt(mensaje.encode())
        return mensaje_encriptado, clave_secreta

    @staticmethod
    def desencriptar(mensaje_encriptado, clave_secreta):
        cipher_suite = Fernet(clave_secreta)
        mensaje_original = cipher_suite.decrypt(mensaje_encriptado).decode()
        return mensaje_original

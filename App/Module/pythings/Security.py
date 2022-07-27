def test():
    print('Test Complete. Pythings Security working.')
    return 'Security Working'

def encrypt(self, text):
    from cryptography.fernet import Fernet
    enckey = Fernet.generate_key()
    fnet = Fernet(enckey)
    enctext = fnet.encrypt(message.encode())
    list = [enctext, enckey]
    return list
def decrypt(self, enctext, enckey):
    from cryptography.fernet import Fernet
    fnet = Fernet(enckey)
    dectext = fnet.decrypt(enctxt).decode()
    return dectext

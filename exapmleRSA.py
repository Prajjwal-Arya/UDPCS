from Crypto.PublicKey import RSA
f = open('/tmp/rsaABkey.pem', 'rb')  
f1 = open('/tmp/rsaABpub.pem', 'rb')  
  
key = RSA.importKey(f.read())  
pubKey = RSA.importKey(f1.read())  

plaintextMessage = "Hello 8gwifi.org"
#RSA Encryption Using Public Key  
cipherText = pubKey.encrypt(plaintextMessage,32)  
print cipherText  
#RSA Decryption Using Private Key  
print key.decrypt(cipherText)
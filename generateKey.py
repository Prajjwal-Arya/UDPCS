from Crypto.PublicKey import RSA  
from Crypto.Util import asn1  
from base64 import b64decode  
  
#Export RSA public/private KEY in PEM format  
key = RSA.generate(2048)  
privKey = key.exportKey('PEM')  
pubKey =  key.publickey().exportKey('PEM')  
  
#save PEM key into the file  
with open('rsaABkey.pem', 'w') as file:  
    file.write(privKey)  
  
with open('rsaABpub.pem', 'w') as file:  
    file.write(pubKey) 
from ecdsa import SigningKey
from ecdsa import VerifyingKey, BadSignatureError

with open("privateBC.pem") as f:
    sk = SigningKey.from_pem(f.read())

sig = sk.sign(b"THIS IS TONYTHIS IS TONYTHIS IS TONYTHIS IS TONY")
with open("signature", "wb") as f:
    f.write(sig)

vk = VerifyingKey.from_pem(open("publicBC.pem").read())
print 'len of Sig :',len(sig)
print 'len of msg :',len("THIS IS TONYTHIS IS TONYTHIS IS TONYTHIS IS TONY")
try:
    vk.verify(sig, b"THIS IS TONYTHIS IS TONYTHIS IS TONYTHIS IS TONY")
    print "good signature"
except BadSignatureError:
    print "BAD SIGNATURE"
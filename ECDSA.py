import ecdsa

# SECP256k1 is the Bitcoin elliptic curve
sk = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1) 
print(sk)
vk = sk.get_verifying_key()
print(vk)
sig = sk.sign(b"message")
print(vk.verify(sig, b"message")) # True
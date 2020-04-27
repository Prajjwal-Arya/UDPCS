from ecdsa import SigningKey,SECP256k1
sk = SigningKey.generate(curve=SECP256k1)
vk = sk.verifying_key
with open("privateBC.pem", "wb") as f:
    f.write(sk.to_pem())
with open("publicBC.pem", "wb") as f:
    f.write(vk.to_pem())
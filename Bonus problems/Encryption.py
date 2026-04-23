def encrypt(m, key):
    return ''.join([chr(ord(a) ^ key) for a in m])

def decrypt(em, key):
    return ''.join([chr(ord(a) ^ key) for a in em])

em = encrypt('Hello, World!', 69)

print(em)
print(decrypt(em, 69))  

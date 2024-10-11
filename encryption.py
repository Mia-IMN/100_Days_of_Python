ciphertext = ""

def vapid(tin, key="LUCKYLION") -> bytes:
    if isinstance(key, str):
        key = key.encode("ascii")
    if isinstance(tin, bytes):
        tin = tin.decode("ascii")
    key_len = len(key)
    ciphertext = []
    for idx, character in enumerate(tin):
        ciphertext.append(int(character) + key[idx % key_len])
    return bytes(ciphertext)

result = vapid("123456789")
print (result)
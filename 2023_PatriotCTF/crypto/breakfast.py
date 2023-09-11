from Crypto.Hash import MD5, SHA224, SHA256, SHA384, SHA512, SHA3_224, SHA3_256, SHA3_384, SHA3_512, TupleHash128, TupleHash256, BLAKE2s, BLAKE2b
import re
import string

flag = 'PCTF'
hasher = None
arr = []
hashes = ['MD5', 'SHA224', 'SHA256', 'SHA384', 'SHA512', 'SHA3_224', 'SHA3_256',
          'SHA3_384', 'SHA3_512', 'TupleHash128', 'TupleHash256', 'BLAKE2s', 'BLAKE2b']
bruter = string.ascii_letters + string.digits + "{}_-@#$%^*"

with open('./BreakfastPasswords.txt', 'r') as f:
    arr = re.findall(r'[0-9a-f]{4,}', f.read())[4:]

assert len(hashes) == len(arr)
for i, _ in enumerate(arr):
    for c in bruter:
        exec(f"hasher = {hashes[i]}.new(); hasher.update(b'{c}')")
        if hasher.hexdigest() == arr[i]:
            flag += c
            break


print(flag)

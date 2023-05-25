# https://book.hacktricks.xyz/macos-hardening/macos-security-and-privilege-escalation
# https://github.com/JohnHammond/ctf-katana


import binascii

def kcpasswd(ciphertext):
    key = '7d895223d2bcddeaa3b91f'
    while len(key) < (len(ciphertext)*2):
        key = key + key
    key = binascii.unhexlify(key)
    result = ''
    for i in range(len(ciphertext)):
        result += chr(ciphertext[i] ^ key[i])
    return result


with open('kcpassword', 'rb') as f:
  c = f.read()

m = kcpasswd(c)
print(m)

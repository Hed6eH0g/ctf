
### kcpassword

![kcpassword](https://github.com/Hed6eH0g/ctf/blob/main/2023/byuctf/forencics/kcpassword/figs/kcpassword_0.png)

A brief survey about kcpasswd tells us that the file is a file that holds the user’s login password if the system owner has enabled automatic login in Mac (see [here](https://book.hacktricks.xyz/macos-hardening/macos-security-and-privilege-escalation)). 

Since the key for kcpasswd is fixed, we can recover it with xoring the key and the ciphertext in accordance with [the code here](https://github.com/JohnHammond/ctf-katana).
```
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
```

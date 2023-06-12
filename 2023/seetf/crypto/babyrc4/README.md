
### BabyRC4


![babyrc4](https://github.com/Hed6eH0g/ctf/blob/main/2023/seetf/crypto/babyrc4/babyrc4_0.png)
 
Since `c0` and `c1` in the given code are the ciphertexts of the flag and `b'a' * 36` encrypted by the common key, we can recover most part of the key by XORing `c1` and `b'a' * 36`.

```
key = urandom(16)
flag = b'SEE{?????????????????????????????????}'[::-1]

def enc(ptxt):
    cipher = ARC4.new(key)
    return cipher.encrypt(ptxt)

print(f"c0 = bytes.fromhex('{enc(flag).hex()}')")
print(f"c1 = bytes.fromhex('{enc(b'a'*36).hex()}')")

"""
c0 = bytes.fromhex('b99665ef4329b168cc1d672dd51081b719e640286e1b0fb124403cb59ddb3cc74bda4fd85dfc')
c1 = bytes.fromhex('a5c237b6102db668ce467579c702d5af4bec7e7d4c0831e3707438a6a3c818d019d555fc')
"""
```

Considering that the flag is set by the inverse order, we can recover the flag as follows:
```
c0 = bytes.fromhex('b99665ef4329b168cc1d672dd51081b719e640286e1b0fb124403cb59ddb3cc74bda4fd85dfc')
c1 = bytes.fromhex('a5c237b6102db668ce467579c702d5af4bec7e7d4c0831e3707438a6a3c818d019d555fc')
print(c0)
print(c1)

flag = ''
for i in range(len(c1)):
  flag = chr(c0[i] ^ c1[i] ^ ord('a')) + flag
print(flag)
```
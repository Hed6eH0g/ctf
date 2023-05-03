
### royal society of arts 2


![rsa2_chall](https://github.com/Hed6eH0g/ctf/blob/main/2023/angstromctf/crypto/royal%20society%20of%20arts%202/royal_society_of_arts_2_0.png)

This challenge allows us to input an arbitrary public key and return the corresponding secret key.
But some inputs such as the plaintext itself or 'actf{xxxxx}' are prohibited and we have to bypass this for the flag.

Since we have the information about `n, e, c` and the plaintext `m` was encrypted by `c = m^e mod n`, a special plaintext `2m` would be obtained by testing `2^e c` as the input.
After that, the flag can recover by dividing `2` as follows:

```
#!/usr/bin/env python3

from pwn import *

host = args.HOST or 'challs.actf.co'
port = int(args.PORT or 32400)

io = connect(host, port)
n = int(str(io.recvline(), 'ascii').strip()[4:])
e = int(str(io.recvline(), 'ascii').strip()[4:])
c = int(str(io.recvline(), 'ascii').strip()[4:])
print(f'n = {n}')
print(f'e = {e}')
print(f'c = {c}')

response = str(io.recvuntil(b'Text to decrypt: '), 'ascii').strip()
payload = (pow(2, e, n) *c)%n
io.sendline(f'{payload}\n'.encode())
response = str(io.recvline(), 'ascii').strip()
print(response)
m = int(response[4:]) // 2

from Crypto.Util.number import long_to_bytes, bytes_to_long

m = long_to_bytes(m)
print(m)
```

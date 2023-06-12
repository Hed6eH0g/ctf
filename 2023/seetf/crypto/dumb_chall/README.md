
### Dumb Chall

![Dumb Chall](https://github.com/Hed6eH0g/ctf/blob/main/2023/seetf/crypto/babyrc4/babyrc4_0.png)

In this challenge, we need to pass 30 rounds of verification.
Since the verification schemes are depending on a request from the server (it means which pair `(r, C)` or `(w, C)` are required without any duplication of `r` and `w`), we have to decide what kind of replies are ideal for the repetitions.

Considering the verification schemes below, `first_verify` and `second_verify` request to input a pair `(w, C)` such that `y^C \equiv g^w \pmod{p}` and a pair `(r, C)` such that `g^r \equiv C \pmod{p}`, respectively.

```
def first_verify(g, p, y, C, w, r) -> bool:
    assert w
    return ((y * C) % p) == pow(g, w, p)

def second_verify(g, p, y, C, w, r) -> bool:
    assert r
    return pow(g, r, p) == C
```

These equivalent equalities concernig `p` allow us to compute `C` with `r = 0, 1, 2, \ldots` or `w = 0, 1, 2, \ldots` depending on the message from the server as follows:

```
from pwn import *

io = remote('win.the.seetf.sg', 3002)

# p
resp = io.recvline().decode().replace('\n', '')
print(resp)
p = int(resp[len('p = '):])

# g
resp = io.recvline().decode().replace('\n', '')
print(resp)
g = int(resp[len('g = '):])

# y
resp = io.recvline().decode().replace('\n', '')
print(resp)
y = int(resp[len('y = '):])

resp = io.recvline().decode().replace('\n', '')
print(resp)
resp = io.recvline().decode().replace('\n', '')
print(resp)


w = 1
r = 1
for i in range(30):
  resp = io.recvuntil(b':').decode()
  print(resp, end='')
  
  if 'w:' in resp:
    print('w')
    C = (pow(g, w, p) * pow(y, -1, p)) % p
    msg = f'{w}'
    io.sendline(msg.encode())
    print('w')
    msg = f'{C}'
    w += 1
    
  if 'r:' in resp:
    print('r')
    C = pow(g, r, p)
    msg = f'{r}'
    io.sendline(msg.encode())
    print('r')
    msg = f'{C}'
    r += 1

  io.sendline(msg.encode())
  resp = io.recvline().decode().replace('\n', '')
  print(resp)

io.interactive()
```
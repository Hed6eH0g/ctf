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

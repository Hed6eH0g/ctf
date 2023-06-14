#!/usr/bin/python3

from pwn import *

io = remote('challs.n00bzunit3d.xyz', 51081)
i = 0
alphabet = "abcdefghijklmnopqrstuvwxyz".upper()
while i < 48:
  resp = io.readuntil('Enter Guess: ').decode()
  print(resp, end='')
  if i%3 == 0:
    s = 3
  elif i%3 == 1:
    s = 5
  elif i%3 == 2:
    s = 7
  io.sendline(str(s).encode())
  resp = io.recvline().decode()
  print(resp)
  
  check = 1
  m = ''
  candidates = [[], [], []]
  # while check > 0:
  for j in range(len(alphabet)):
    k = 1
    while ((s << 16) - ord(alphabet[j])*k) > 0:
      check = ((s << 16) - ord(alphabet[j])*k)
      if check == int(resp):
        # print(alphabet[j], end='')
        candidates[i%3].append(alphabet[j])
        check = -1
      k += 1

  print(candidates[i%3])
  print('')
  i += 1
  
print(m)
resp = io.readuntil('Enter Guess: ').decode()
print(resp, end='')
# io.sendline(m.encode())

io.interactive()

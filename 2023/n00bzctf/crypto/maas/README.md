### MaaS

![MaaS](https://github.com/Hed6eH0g/ctf/blob/main/2023/n00bzctf/crypto/maas/maas_0.png)


The server in this challenge provides the results of `(s<<16) \pmod{r_i}`, where `x` is a digit given to the server and `r_i` is an $i$-th element of a sequence `r = {ord(x_i)}` consisting of randomly chosen `x_i` from `'abcdefghijklmnopqrstuvwxyz'.upper()`.
Since we can get the results of different messages with the same modulo at most 3 times, the moduli are able to presume by exploring the correponding capital letter such that `(s<<16) \pmod{r_i} = ((s << 16) - ord(alphabet[j])*k)`, where `alphabet='abcdefghijklmnopqrstuvwxyz'.upper()` and `k \leq 1`

Though we have to find out the sequence of moduli from the results, we sometimes found that there sometimes exists an empty set or a different letter set for the result for the same moduli.
Thus, we decided to presume the sequence of moduli manually after observing the entire results as follows:
```
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
```
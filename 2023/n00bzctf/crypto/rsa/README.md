### RSA


![RSA](https://github.com/Hed6eH0g/ctf/blob/main/2023/n00bzctf/crypto/rsa/rsa_0.png)
 
Though `e` is a little bit large for a usual case, this is a typical vulnerable example against Hastand's broadcast attack.
```
import gmpy2
from Crypto.Util.number import long_to_bytes
from pwn import *

import gmpy2
gmpy2.get_context().precision = 4096     

from binascii import unhexlify
from functools import reduce
from gmpy2 import root

# Håstad's Broadcast Attack
# https://id0-rsa.pub/problem/11/        

# Resources
# https://en.wikipedia.org/wiki/Coppersmith%27s_Attack
# https://github.com/sigh/Python-Math/blob/master/ntheory.py

def chinese_remainder_theorem(items):    
    # Determine N, the product of all n_i
    N = 1
    for a, n in items:
        N *= n

    # Find the solution (mod N)
    result = 0
    for a, n in items:
        m = N // n
        r, s, d = extended_gcd(n, m)     
        if d != 1:
            raise "Input not pairwise co-prime"
        result += a * s * m

    # Make sure we return the canonical solution.
    return result % N


def extended_gcd(a, b):
    x, y = 0, 1
    lastx, lasty = 1, 0

    while b:
        a, (q, b) = b, divmod(a, b)      
        x, lastx = lastx - q * x, x      
        y, lasty = lasty - q * y, y      

    return (lastx, lasty, a)


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


def get_value(filename):
    with open(filename) as f:
        value = f.readline()
    return int(value, 16)

if __name__ == '__main__':

    n = []
    ct = []
    i = 0
    while len(n) < 17:
      io = remote('challs.n00bzunit3d.xyz', 2069)
      response = io.recvline().decode().replace('\n', '')
      e = int(response[len('e = '):])
      # print(response)
      response = io.recvline().decode().replace('\n', '')
      cti = int(response[len('ct = '):])
      # print(response)
      response = io.recvline().decode().replace('\n', '')
      ni = int(response[len('n = '):])
      
      if (ni not in n) and (cti not in ct):
        n.append(ni)
        ct.append(cti)


    ciphertexts = ct
    modulus = n
    C = chinese_remainder_theorem([(ct[i], n[i]) for i in range(len(n))])
    M = int(root(C, e))

    print(long_to_bytes(M))
```

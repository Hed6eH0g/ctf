

### dsa?


![https://github.com/Hed6eH0g/ctf/blob/main/2023/wanictf/crypto/dsa/dsa_0.png]

This challenge is based on the RSA digital signature.
We can get values `p, q, g, y , h=Hash(m), r, s` by connecting the server (dsa-cry.wanictf.org on port 50010), where `m` is the flag and `s` denotes a signature.

According to the signature procedure, we can deal with `p, q, g, h, r` as constant values and `y, s` are random variables.
In addition, since `s = m(h + xr) = mh + mxr \pmod{q}`, gathering several signatures allows us to have the following equations.
$$s_1 - s_2 = m(x_1 - x_2)r,$$ 
$$s_2 - s_3 = m(x_2 - x_3)r,$$ 
$$s_3 - s_4 = m(x_3 - x_4)r,$$
$$\vdots$$

Thus, one can find that the gcd of the above equations gives us the desired flag.

```
import math
from pwn import *
from Crypto.Util.number import bytes_to_long, getPrime, long_to_bytes


def get_sign():
  io = remote("dsa-cry.wanictf.org", 50010)
  resp = io.recvall().decode()
  # print(resp)
  lines = resp.split('\n')
  p = int(lines[0][4:])
  q = int(lines[1][4:])
  g = int(lines[2][4:])
  y = int(lines[3][4:])
  # _ = lines[4]
  h = int(lines[5][15:], 16)
  r = int(lines[6][4:])
  s = int(lines[7][4:])
  
  print(f'p: {p}')
  print(f'q: {q}')
  print(f'g: {g}')
  print(f'y: {y}')
  print(f'h: {h}')
  print(f'r: {r}')
  print(f's: {s}')
  print('')

  return p, q, g, y, h, r, s


ys = []
signs = []
mxs = []
for i in range(10):
  p, q, g, y, h, r, s1 = get_sign()
  _, _, _, y, _, _, s2 = get_sign()
  mx = (((s1 - s2) % q) * pow(r, -1, q)) % q
  if mx < pow(2, 48*16):
    mxs.append(mx)

  # print(f'p: {p}')
  # print(f'q: {q}')
  # print(f'g: {g}')
  # print(f'y: {y}')
  # print(f'h: {h}')
  # print(f'r: {r}')
  # print(f's: {s}')

m = math.gcd(math.gcd(mxs[0], mxs[1]), mxs[2])
print(long_to_bytes(m))
```

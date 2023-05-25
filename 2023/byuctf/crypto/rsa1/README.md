
### RSA1

![RSA1](https://github.com/Hed6eH0g/ctf/blob/main/2023/byuctf/crypto/rsa1/figs/rsa1_0.png)

Since `n` is factorized into `n = 15631612382272805561 * 18413880828441662521`, we can compute `\phi(n)` and recover the flag as follows:
```
n = 287838647563564518717519107521814079281
e = 7
c = 258476617615202392748150555415953446503

from Crypto.Util.number import long_to_bytes

p = 15631612382272805561
q = 18413880828441662521

phi = (p-1)*(q-1)
d = pow(e, -1, phi)
m = pow(c, d, n)
print(long_to_bytes(m))
```

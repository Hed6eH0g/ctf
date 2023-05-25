
### RSA5

![RSA5](https://github.com/Hed6eH0g/ctf/blob/main/2023/byuctf/crypto/rsa5/figs/rsa5_0.png)

Since we have several pairs of different public keys `e1, e2` and ciphertexts `c1,c2` which were encrypted under the same modulus `n`, we can apply common modulus attack.

[This repository](https://github.com/HexPandaa/RSA-Common-Modulus-Attack/blob/master/rsa-cm.py) gives us the exact solver and we could get the flag with it.

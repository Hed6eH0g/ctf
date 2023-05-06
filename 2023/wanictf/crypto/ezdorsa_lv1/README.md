
### EZDORSA_Lv1

![ezdorsa_lv1](https://github.com/Hed6eH0g/ctf/blob/main/2023/wanictf/crypto/ezdorsa_lv1/EZDORSA_Lv1_0.png)

This challenge requests us to find $m$ such that the ciphertext is being $10$.
We can explore with the following python code.
```
p = 3
q = 5
n = p*q
e = 65535

m = 1
c = 1
while c != 10:
  m += 1
  c = pow(m, e, n)
print(m)
```

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








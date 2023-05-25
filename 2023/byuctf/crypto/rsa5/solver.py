
# https://github.com/HexPandaa/RSA-Common-Modulus-Attack/blob/master/rsa-cm.py

#!/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "HexPandaa"


from Crypto.PublicKey import RSA
from Crypto.Util.number import (
  long_to_bytes,
  bytes_to_long,
  GCD
)
import gmpy2
from base64 import b64decode

import sys


# Source: https://crypto.stackexchange.com/a/60404
def bytes_to_integer(data):
    output = 0
    size = len(data)
    for index in range(size):
        output |= data[index] << (8 * (size - 1 - index))
    return output


def integer_to_bytes(integer, _bytes):
    output = bytearray()
    for byte in range(_bytes):
        output.append((integer >> (8 * (_bytes - 1 - byte))) & 255)
    return output


# Source: https://github.com/ashutosh1206/Crypton/blob/master/RSA-encryption/Attack-Common-Modulus/exploit.py
def egcd(a, b):
    if (a == 0):
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


# Calculates a^{b} mod n when b is negative
def neg_pow(a, b, n):
    assert b < 0
    assert GCD(a, n) == 1
    res = int(gmpy2.invert(a, n))
    res = pow(res, b*(-1), n)
    return res


# e1 --> Public Key exponent used to encrypt message m and get ciphertext c1
# e2 --> Public Key exponent used to encrypt message m and get ciphertext c2
# n --> Modulus
# The following attack works only when m^{GCD(e1, e2)} < n
def common_modulus(e1, e2, n, c1, c2):
    g, a, b = egcd(e1, e2)
    if a < 0:
        c1 = neg_pow(c1, a, n)
    else:
        c1 = pow(c1, a, n)
    if b < 0:
        c2 = neg_pow(c2, b, n)
    else:
        c2 = pow(c2, b, n)
    ct = c1*c2 % n
    m = int(gmpy2.iroot(ct, g)[0])
    return m


def main():

    n = 158307578375429142391814474806884486236362186916188452580137711655290101749246194796158132723192108831610021920979976831387798531310286521988621973910776725756124498277292094830880179737057636826926718870947402385998304759357604096043571760391265436342427330673679572532727716853811470803394787706010603830747
    
    e1 = 65537
    c1 = 147465654815005020063943150787541676244006907179548061733683379407115931956604160894199596187128857070739585522099795520030109295201146791378167977530770154086872347421667566213107792455663772279848013855378166127142983660396920011133029349489200452580907847840266595584254579298524777000061248118561875608240
    
    e2 = 65521
    c2 = 142713643080475406732653557020038566547302005567266455940547551173573770529850069157484999432568532977025654715928532390305041525635025949965799289602536953914794718670859158768092964083443092374251987427058692219234329521939404919423432910655508395090232621076454399975588453154238832799760275047924852124717

    m = common_modulus(e1, e2, n, c1, c2)
    m = long_to_bytes(m)
    print(m)


if __name__ == '__main__':
    main()

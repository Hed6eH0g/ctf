
### Collision


![Collision](https://github.com/Hed6eH0g/ctf/blob/main/2023/byuctf/misc/collision/figs/collision_0.png)

A brief look at the entire process of the code (`verify.py`), it was found that two inputs (pic1 and pic2) are verified in the following points:
    1. are the inputs valid as PNG files?
    2. are the MD5 hash values of two inputs the same?
    3. do the inputs contain specific sentences?

At a glance, we wondered that this challenge requests for finding the different pre-images that cause a collision throughout the MD5 hash function.

But, we realized that there are no rules for the same input for pic1 and pic2.
Thus, the following code was made for generating an adequate text and we input it twice via nc to obtain the flag. 
```
from pwn import *
import hashlib
import base64

base_str_1 = "Keeping your software and systems up-to-date with the latest security patches is a crucial step in safeguarding against potential cyber attacks."
base_str_2 = "Implementing strong passwords, two-factor authentication, and regular employee training are essential measures in maintaining a secure digital environment for your organization."

txt1 = b'\x89PNG\r\n\x1a\n' + base_str_1.encode() + base_str_2.encode()

print(base64.b64encode(txt1)) 
```

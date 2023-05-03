
### ranch

![problem](https://github.com/Hed6eH0g/ctf/blob/main/2023/angstromctf/crypto/ranch/ranch0.png)

This challenge asks us to decrypt the given encrypted flag.
According to `ranch.py`, each ASCII character in the flag was shifted with a certain integer, which is loaded from `secret_shift.txt`.
Since we know the flag format is `actf{XXXXX}`, we can presume the value of `shift` as `17` from `rtkw`.
So we can recover the flag as `actf{lo0ks_like_we'll_h4ve_to_try_an0ther_dress1ng_5ef89b3a44901831}` with the following script.

```
import string                                                                                                                                                                                                                               
                                                                                                                                                                                                                                            
enc_flag = "rtkw{cf0bj_czbv_nv'cc_y4mv_kf_kip_re0kyvi_uivjj1ex_5vw89s3r44901831}"     
shift = -17                                                                                                                                                            
                                                                                                                                                                                                                                             
for i in enc_flag:                                                                                                                                                                                                                                 
    if i in string.ascii_lowercase:                                                                                                                                                                                                         
        flag += chr(((ord(i) - 97 +shift) % 26)+97)                                                                                                                                                                                   
    else:                                                                                                                                                                                                                                   
        flag += i                                                                                                                                                                                                                      
                                                                                                                                                                                                                                            
print(flag)   
```

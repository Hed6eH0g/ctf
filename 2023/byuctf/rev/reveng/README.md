
### RevEng

![RevEng](https://github.com/Hed6eH0g/ctf/blob/main/2023/byuctf/rev/reveng/figs/reveng_0.png)

Opening with [IDA Free](https://hex-rays.com/ida-free/) allowed us to find `lea     rax, passphrase_encrypted ; "Xmj%yzwsji%rj%nsyt%f%sj|y"`.
Since [dCode](https://www.dcode.fr/en) has a cipher identifier, we could try to check which encryption scheme is used for `Xmj%yzwsji%rj%nsyt%f%sj|y`.
Then, it was found that the ciphertext seems to be encrypted by ASCII shift cipher and it would be decrypted to `She turned me into a newt`.
Then, running gettingBetter with the password gives us the flag.

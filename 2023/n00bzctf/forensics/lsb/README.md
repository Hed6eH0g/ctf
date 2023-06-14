### LSB

![LSB](https://github.com/Hed6eH0g/ctf/blob/main/2023/n00bzctf/forensics/lsb/lsb_0.png)

A brief search with keywords "wav" and "lsb" leaded us [this repository](https://github.com/ragibson/Steganography) and following by the instruction there, the flag was extracted with `stegolsb wavsteg -r -i chall.wav -o output.txt -n 2 -b 1000`.
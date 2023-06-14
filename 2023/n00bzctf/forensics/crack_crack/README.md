### Crack & Crack

![Crack & Crack](https://github.com/Hed6eH0g/ctf/blob/main/2023/n00bzctf/corensics/crack_crack/crack_crack_0.png)


As the title stands for, we have to crack passwords twice in this challenge.
The first target is a zip file and there is a famous tool `john` for cracking a password hash.
For this, a password hash file of the given zip file is required for brute-forcing the password, and this can be done by `zip2john` as `zip2john flag.zip > zip.hash`.
Then, `john zip.hash --wordlist=rockyou.txt` allows us to find a password (`1337h4x0r`) and we can extract a pdf file from the zip file.

Second, the pdf file is also locked by a password.
As well as in the previous case, we can extract the password hash of the pdf by `pdf2john flag.pdf > pdf.hash` and attack it by `john pdf.hash --wordlist=rockyou.txt`.
Then, we got the password (`noobmaster`) for the pdf and the flag.
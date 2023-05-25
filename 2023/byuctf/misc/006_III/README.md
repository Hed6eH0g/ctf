
### 006 III

![006 III](https://github.com/Hed6eH0g/ctf/blob/main/2023/byuctf/misc/006_III/figs/006_III_0.png)

This challenge requests us to recover the flag from 4 different hash values.
The corresponding texts for the first two (`6328C530F895CA13C75E161DEC260EC2C0BED4FCFF1B34448EA16A7FFFFA5CDC403E5CC83B23321E9AD3280952BE2ADB037DD7AFA3084B7E940C6A655B2F13BA` and `3FAE7E18F9004673D0E68CA10264A1ABAF76FBF42E60D960A1B95289401146E4BF39E599641C730DB8F664F7F1DD02F171BEB4730AC756AAC7CF40C6BC4D623A`) hashes could be found with the CrackStation but the remaining two could not be recovered immediately.

So, we decided to change the tool to crack the hash.
The next choice for this was to attack those hashes by `john` or `hashcat` with a wordlist `rockyou.txt`.
But unfortunately, they could not reveal the plaintexts.

Thus, again we search an online tool for hash cracking and found that [Hashes.com](https://hashes.com/en/decrypt/hash) allows us to both remaining hashes into the corresponding plaintexts.

Consequently, we found the flag `byuctf{goldeneye007_goldeneye641_goldeneye069_goldeneye159}`.

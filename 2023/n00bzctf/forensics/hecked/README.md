### Hecked

![Hecked](https://github.com/Hed6eH0g/ctf/blob/main/2023/n00bzctf/forensics/hecked/hecked_0.png)

Open the given pcap file with WireShark and follow the TCP stream allows us to find the sequence of messages below.
![pcap1](https://github.com/Hed6eH0g/ctf/blob/main/2023/n00bzctf/forensics/hecked/hecked_1.png)
![pcap2](https://github.com/Hed6eH0g/ctf/blob/main/2023/n00bzctf/forensics/hecked/hecked_2.png)
![pcap3](https://github.com/Hed6eH0g/ctf/blob/main/2023/n00bzctf/forensics/hecked/hecked_3.png)

Since the flag is endowed by `echo -n vulnerableService_serviceVersion_attackersFirstBashCommandOnHackedServer | md5sum`, we can get the flag by replacing the corresponding substrings with `echo -n vsFTPd_2.3.4_id | md5sum`.
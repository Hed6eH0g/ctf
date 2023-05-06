
### beg_for_a_peg


![beg_for_a_peg](https://github.com/Hed6eH0g/ctf/blob/main/2023/wanictf/forensics/beg_for_a_peg/beg_for_a_peg_0.png)

This challenge gave us a pcap file, thus, we opened it with wireshark.
By following the TCP stream, we can find that three distinct JPG files are communicated and one of them is flag.jpg as shown below.

![beg_for_a_peg_1](https://github.com/Hed6eH0g/ctf/blob/main/2023/wanictf/forensics/beg_for_a_peg/beg_for_a_peg_1.png)

Thus, we save the TCP stream as Raw format but it could not open as a JPG file as it is.
This is because it includes the HTTP header.
We remove it from the file and this allows us to open it with an image viewer.

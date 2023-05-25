

### Leet 1


![Leet_1](https://github.com/Hed6eH0g/ctf/blob/main/2023/byuctf/jail/leet_1/figs/leet_1_0.png)


In this challenge, we need to give an input that matches `1337` though the input consisting of digits seems to be prohibited.

Since we can give a literal or a text string with a conversion into an integer throughout `eval`, we guessed that `ord()` can be a candidate for this.

So we checked the [official documentation](https://python-reference.readthedocs.io/en/latest/docs/functions/ord.html) and found that there exists a specific python environment that allows one to input a literal which is represented by an integer in the range `[0..65535]` (according to "If a unicode argument is given and Python was built with UCS2 Unicode, then the character’s code point must be in the range `[0..65535]` inclusive").

Then, searching the list of ucs2 unicode brought [this page](http://www.columbia.edu/kermit/ucs2.html) and found that the literal `'Թ' (0x0539)` is the one we desired.

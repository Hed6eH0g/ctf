
### directory


![directory_chall](https://github.com/Hed6eH0g/ctf/blob/main/2023/angstromctf/web/directory/directory0.png)

There are many directories named numeric number in incremental order.
Though it takes a while to complete running, accessing each directory turn by turn is straightforward and it would be easy to implement and run it in the background.	

```
#!/usr/bin/env python3

import time
import requests

url = 'https://directory.web.actf.co/'

for i in range(10000):
  url_i = url + f'{i}.html'
  print(url_i)
  res = requests.get(url_i)
  # print(res.status_code)  # 200
  # print(res.text)
  # print('')
  # print(' ---- ')
  # print('')
  
  if 'actf' in res.text:
    break
```

### xkcd 2637

![xkcd 2637](https://github.com/Hed6eH0g/ctf/blob/main/2023/byuctf/misc/xkcd_2637/figs/xkcd_2637_0.png)


A brief survey about "xkcd 2637" noticed us that it seems to be [Roman Numerals](https://www.explainxkcd.com/wiki/index.php/2637:_Roman_Numerals).
There are less repositries that look nice for solving this problem.
Further survey on the internet brought [this post](https://codereview.stackexchange.com/questions/80496/adding-two-roman-numeral-inputs) and thus, we got the python implementation of Roman Numerals including the conversions.
Based on the codes, we made the following codes and solving 500 problems allowed us to obtain the flag. 
```
from pwn import *

_roman_digits = [
    (1, 'I'),
    (4, 'IV'),
    (5, 'V'),
    (9, 'IX'),
    (10, 'X'),
    (40, 'XL'),
    (50, 'L'),
    (90, 'XC'),
    (100, 'C'),
    (400, 'CD'),
    (500, 'D'),
    (900, 'CM'),
    (1000, 'M'),
][::-1] # process digits from highest to lowest


def replace_input_to_roman(input_str):
    roman_txt = input_str.replace('1000', 'M').replace('900', 'CM').replace('500', 'D').replace('400', 'CD').replace('100', 'C').replace('90', 'XC').replace('50', 'L').replace('40', 'XL').replace('10', 'X').replace('9', 'IX').replace('5', 'V').replace('4', 'IV').replace('1', 'I')

    return roman_txt

def replace_roman_to_output(input_str):
    output_txt = input_str.replace('M', '1000').replace('CM', '900').replace('D', '500' ).replace('CD', '400').replace('C', '100').replace('XC', '90').replace('L', '50').replace('XL', '40').replace('X', '10').replace('IX', '9').replace('V', '5').replace('IV', '4').replace('I', '1')
    return output_txt


def roman_to_decimal(roman):      
    original = roman
    roman = roman.upper() # allow upper and lower case
    decimal = 0
    for digit in _roman_digits:   
        while roman.startswith(digit[1]):
            roman = roman[len(digit[1]):] # discard current digit...
            decimal += digit[0] # ...and add it to result
    if roman: raise ValueError('{} is not a valid roman numeral'.format(original))
    return decimal


def decimal_to_roman(decimal):    
    original = decimal
    roman = ''
    for digit in _roman_digits:   
        while decimal >= digit[0]:
            decimal -= digit[0] # discard current digit...
            roman += digit[1] # ...and add it to result
    if decimal: raise ValueError('{} could not be converted to a roman numeral'.format(original))     
    return roman


io = remote('byuctf.xyz', 40014)  
context.log_level = 'debug'       

response = io.recvuntil(b'Get 500 problems correct to get the flag!\n').decode()
print(response)

for i in range(500):
  response = io.recvuntil(b'= ').decode()
  print(response)
  response = response[:-2].split(' ')
  a = roman_to_decimal(replace_input_to_roman(response[0]))
  b = roman_to_decimal(replace_input_to_roman(response[2]))
  if response[1] == '+':
    c = decimal_to_roman(a + b)   
  elif response[1] == '-':        
    c = decimal_to_roman(a - b)   
  elif response[1] == '*':        
    c = decimal_to_roman(a * b)   
  else:
    exit(1)
  answer  = replace_roman_to_output(c)
  print(answer)
  io.sendline(answer.encode())    

io.interactive()
```

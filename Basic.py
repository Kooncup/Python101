Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> name = 'Panupong'
>>> print(name)
Panupong
>>> type(name)
<class 'str'>
>>> name.lower()
'panupong'
>>> name.upper()
'PANUPONG'
>>> friend = 'First'
>>> print('สวัสดีFirst สบายดีไหม?')
สวัสดีFirst สบายดีไหม?
>>> print('สวัสดี'+friend+'สบายดีไหม?')
สวัสดีFirstสบายดีไหม?
>>> money = 10
>>> type(money)
<class 'int'>
>>> print(friend+'ยืมเงืน '+str(money)+' บาท')
Firstยืมเงืน 10 บาท
>>> print('{}ยืมเงิน {} บาท'.format(friend,money))
Firstยืมเงิน 10 บาท
>>> print(f'{friend}ยืมเงิน {money} บาท')
Firstยืมเงิน 10 บาท
>>> money = 100000000
>>> print(f'{money:,}')
100,000,000
>>> print(f'{money:,.2f}')
100,000,000.00
>>> print('{:,.2f}'.format(money))
100,000,000.00
>>> import math
>>> math.log10
<built-in function log10>
>>> math.log10(5)
0.6989700043360189
>>> from datetime import datetime
>>> datetime.now
<built-in method now of type object at 0x00007FF85B3D8980>
datetime.now()
datetime.datetime(2023, 2, 12, 21, 15, 36, 89174)
datetime.now.strftime('%d%m%Y %H:%M:%S')
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    datetime.now.strftime('%d%m%Y %H:%M:%S')
AttributeError: 'builtin_function_or_method' object has no attribute 'strftime'
datetime.now().strftime('%d%m%Y %H:%M:%S')
'12022023 21:17:37'
import random
random.ranint(1,7)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    random.ranint(1,7)
AttributeError: module 'random' has no attribute 'ranint'. Did you mean: 'randint'?
random.randint(1,7)
2
store = ['ป้าส้ม','ป้าตู่','ป้าป้อม','ป้าชูวิทย์']
random.randstr(store)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    random.randstr(store)
AttributeError: module 'random' has no attribute 'randstr'
random.choice(store)
'ป้าตู่'

# coding: utf-8
import string
d = {}
for ch in list(string.ascii_lowercase):
    d[ch] = 0
    
while True:
    try:
        s = list(input().lower())
    except EOFError:
        break
    
    
    for ch in s:
        if ch.isalpha():
            d[ch] += 1
        else:
            pass
    

for k, v in sorted(d.items()):
    print('{} : {}'.format(k, v))


import random

s = input()

len_s = len(s)

if len_s==3:
	num = 0
else:
	num = random.randint(0,len_s-4)

name = s[num]+s[num+1]+s[num+2]

print(name)
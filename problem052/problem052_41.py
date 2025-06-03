# -*- coding:utf-8 -*-
n = int(input())
s=''

for i in range(1,n+1):
    if i%3==0 or i%10==3:
        s = s + " " + str(i)
        continue
    else:
        x = i
        while x >0:
            x //= 10
            if x%10==3: 
                s = s + " " + str(i)
                break
print(s)
# -*- coding: utf-8
s = list(map(str,input().split()))
sum = 0
for i in range(len(s)):
    sum += (int) (s[i])
if sum %9 == 0:
    print("Yes")
else:
    print("No")
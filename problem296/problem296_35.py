s = input()
k = int(input())
import collections
co = collections.Counter(list(s))
n = len(s)
if len(co.values())==1:
    print(n*k//2)
    exit()
prev = ""
cnt = 0
for i in range(n):
    if s[i] == prev:
        cnt+=1
        prev=""
    else:
        prev=s[i]
bf = 0
af = 0
if s[0] == s[-1]:
    for i in range(n):
        if s[i] ==s[0]:
            bf+=1
        else:break
    for i in range(n):
        if s[-i-1] ==s[-1]:
            af+=1
        else:break
cnt = cnt - (bf//2 + af//2)
print(cnt*k + (bf+af)//2 *(k-1) +bf//2 + af//2)

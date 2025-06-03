from itertools import groupby
s = input()
k = int(input())
if len(set(s)) == 1:
    print(len(s)*k//2)
    exit()
g = [len(list(v)) for _, v in groupby(s)]
ans = sum(i//2 for i in g)*k
if s[0] != s[-1]:
    print(ans)
    exit()
a, *_, b = g
ans -= (a//2 + b//2 - (a+b)//2)*(k-1)
print(ans)

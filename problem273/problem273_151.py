from collections import defaultdict
from sys import stdout
printn = lambda x: stdout.write(x)
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
DBG = True  and False
BIG = 999999999
R = 10**9 + 7

def ddprint(x):
  if DBG:
    print(x)

n,k = inm()
a = inl()
h =defaultdict(int)
b = [0]*(n+1)
s = [0]*(n+1)
for i in range(n):
    s[i+1] = s[i]+a[i]
    b[i+1] = (s[i+1]-i-1)%k
ddprint(s)
ddprint(b)
acc = 0
for i in range(n+1):
    if i>=k:
        h[b[i-k]] -= 1
    acc += h[b[i]]
    h[b[i]] += 1
    #ddprint("i {} acc {} h {}".format(i,acc,h))
print(acc)

#from collections import deque,defaultdict
printn = lambda x: print(x,end='')
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
ins = lambda : input().strip()
DBG = True # and False
BIG = 10**18
R = 10**9 + 7
#R = 998244353

def ddprint(x):
  if DBG:
    print(x)

s = ins()
t = ins()
ls = len(s)
lt = len(t)
mn = BIG
for i in range(ls-lt+1):
    x = 0
    for j in range(lt):
        if s[i+j]!=t[j]:
            x += 1
    mn = min(mn,x)
print(mn)

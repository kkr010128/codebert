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

n,k,c = inm()
s = ins()
l = [0]*n
r = [0]*n
for i in range(n):
    if s[i]=='x':
        l[i] = l[max(0,i-1)]
    else:
        l[i] = max(l[max(0,i-1)], (l[i-c-1]+1) if i>c else 1)
for i in range(n-1,-1,-1):
    if s[i]=='x':
        r[i] = r[min(n-1,i+1)]
    else:
        r[i] = max(r[min(n-1,i+1)], (r[i+c+1]+1) if i<n-c-1 else 1)
#ddprint(l)
#ddprint(r)
ans = []
for i in range(n):
    if s[i]=='o' and \
       (l[i-1] if i>0 else 0)+(r[i+1] if i<n-1 else 0)==k-1:
        ans.append(i+1)
for x in ans:
    print(x)

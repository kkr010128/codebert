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

a,b,c = inm()
k = inn()
x = 0
while b<=a:
  b *= 2
  x += 1
while c<=b:
  c *= 2
  x += 1
print('Yes' if x<=k else 'No')


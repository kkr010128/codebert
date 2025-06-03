from sys import stdout
printn = lambda x: stdout.write(str(x))
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
ins = lambda : input().strip()
DBG = True  and False
BIG = 999999999
R = 10**9 + 7

def ddprint(x):
  if DBG:
    print(x)

n,t = inm()
ab = []
for i in range(n):
    aa,bb = inm()
    ab.append((aa,-bb))
ab.sort()
d = [ [-1]*(t+1) for i in range(n+1) ]
for i in range(n+1):
    d[i][0] = 0
#ddprint(d)
for i in range(n):
    for j in range(t+1):
        d[i+1][j] = max(d[i+1][j], d[i][j])
        if j<t and d[i][j]>=0:
            s = min(t,j+ab[i][0])
            d[i+1][s] = max(d[i+1][s], d[i][j]-ab[i][1])
if DBG:
    for i in range(n):
        printn(i)
        ddprint(d[i])
mx = 0
for j in range(t,-1,-1):
    if d[n][j]>=0:
        mx = max(mx,d[n][j])
print(mx)

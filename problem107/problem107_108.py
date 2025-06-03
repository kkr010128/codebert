import sys
sys.setrecursionlimit(10**8)
N = int(input())
X = input()
if X == '0':
    for _ in range(N):
        print(1)
        exit()

mem = [None] * (200005)
mem[0] = 0
def f(n):
    if mem[n] is not None: return mem[n]
    c = bin(n).count('1')
    r = 1 + f(n%c)
    mem[n] = r
    return r

for i in range(200005):
    f(i)

cnt = X.count('1')
a,b = cnt+1, cnt-1

ans = [None] * N

n = 0
for c in X:
    n *= 2
    n += int(c)
    n %= a
for i,c in reversed(list(enumerate(X))):
    if c=='1': continue
    ans[i] = mem[(n+pow(2,N-i-1,a))%a] + 1

if b:
    n = 0
    for c in X:
        n *= 2
        n += int(c)
        n %= b
    for i,c in reversed(list(enumerate(X))):
        if c=='0': continue
        ans[i] = mem[(n-pow(2,N-i-1,b))%b] + 1
else:
    for i in range(N):
        if ans[i] is None:
            ans[i] = 0

print(*ans, sep='\n')
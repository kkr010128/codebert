n,k = map(int, input().split())
s = list(map(int,input().strip().split()))

t = 0
ss = sorted(s)
for kk in range(k):
    t += ss[kk]
print(t)
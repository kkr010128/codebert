n,k,s = map(int,input().split())
if s == 10**9:
    t = 1
else:
    t = s+1
ls = [t]*n
for i in range(k):
    ls[i] = s
print(*ls)
n,k,s = map(int, input().split())
if s!=10**9:
    x = [10**9]*n
else:
    x = [1]*n

for i in range(k):
    x[i]=s
print(*x)

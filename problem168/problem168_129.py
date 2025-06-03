n,m = map(int,input().split())
a = list(map(int,input().split()))
for v in a:
    n = n - v
    if n < 0:
        n = -1
        break
print(n)
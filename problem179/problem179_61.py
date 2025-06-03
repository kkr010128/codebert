n,m = map(int,input().split())
a = sorted(list(map(int, input().split())),reverse=True)
total = sum(a) / (4 * m)
if min(a[:m]) >= total:
    print("Yes")
else:
    print("No")
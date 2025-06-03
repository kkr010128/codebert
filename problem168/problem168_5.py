n, m = map(int, input().split())
am = list(map(int, input().split()))

if n-sum(am) < 0:
    print(-1)
else:
    print(n-sum(am))
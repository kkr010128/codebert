n, m = map(int, input().split())
work = list(map(int, input().split()))

if n - sum(work) < 0:
    print("-1")
else:
    print(n - sum(work))

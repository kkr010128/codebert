n, m = map(int, input().split())

a = list(map(int, input().split()))

s = int(sum(a))

if n > s:
    print(n-s)
elif n == s:
    print(0)
else:
    print(-1)

n, m = map(int, input().split())
a = list(map(int, input().split()))

for time in a:
    n -= time
    if n<0:
        n = -1
        break

print(n)
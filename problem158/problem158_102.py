n = int(input())
a, b = map(int, input().split())
i = 0
ans = "NG"
while i <= b:
    if i >= a and i % n == 0:
        ans = "OK"
    i += n

print(ans)

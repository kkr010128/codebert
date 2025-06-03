k = int(input())
a, b = map(int, input().split())

i = 1
ans = "NG"
while k*i <= b:
    if a <= k*i:
        ans = "OK"
        break
    i += 1
print(ans)
x = int(input())

ans = 0

while True:
    ans += 1
    if ans*x % 360 == 0:
        break

print(ans)

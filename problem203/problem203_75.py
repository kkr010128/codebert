a, b = map(int, input().split())
ans = -1

for money in range(pow(10, 4)):
    if int(money*0.08) == a and int(money*0.1) == b:
        ans = money
        break

print(ans)
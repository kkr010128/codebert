X = int(input())

ans = 0
num = 100
while X > num:
    num = num+num//100
    ans += 1

print(ans)
x = int(input())

Level = [i for i in range(400, 2000, 200)]

ans = 9
for level in Level:
    if x >= level:
        ans -= 1
print(ans)
X = int(input())

ans = 1

while (X*ans)%360 != 0:
    ans += 1
print(ans)

X = int(input())
t = X
ans = 1
while t%360 != 0:
    t += X
    ans += 1
print(ans)

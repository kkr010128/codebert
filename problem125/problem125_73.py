X = int(input())
P = 360
ans = 1
x = X
while x%P != 0:
    ans += 1
    x += X
print(ans)

H = int(input())
num = 1
ans = 0
while H > 0:
    H //= 2
    ans += num
    num *= 2
print(ans)
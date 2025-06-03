n = int(input())
ans = 100000
# ans += (n*(100000*0.05))
for i in range(n):
    ans *= 1.05
    if ans % 1000 > 0:
        ans = ans // 1000 * 1000 + 1000
print(int(ans))

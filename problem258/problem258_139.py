# 解説見ました。
n = int(input())
ans = 0
if n%2 == 0:
    m = 1
    for _ in range(25):
        ans += n//(m*10)
        m *= 5
print(ans)
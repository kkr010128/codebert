_ = int(input())
S = list(map(int, input().split()))
_ = int(input())
T = list(map(int, input().split()))

ans = 0
for i in T:
    if i in S:
        ans += 1
print(ans)

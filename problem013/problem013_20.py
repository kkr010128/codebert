n = int(input())
R = [int(input()) for _ in range(n)]
ans = R[1] - R[0]
bottom = min(R[0], R[1])
for i in range(2, n):
    ans = max(ans, R[i] - bottom)
    if R[i] < bottom:
        bottom = R[i]
print(ans)
n = int(input().rstrip())
R = [0 for _ in range(n)]
for i in range(n):
    R[i] = int(input().rstrip())

margin = - 10**9
min_R = R[0]
for j in range(1, n):
    margin = max(margin, R[j] - min_R)
    min_R = min(min_R, R[j])

print(margin)

#93 B - Iron Bar Cutting WA (hint)
N = int(input())
A = list(map(int,input().split()))

# 差が最小の切れ目を見つける
length = sum(A)
left = 0
dist = 0
mdist = length
midx = 0
for i,a in enumerate(A):
    left += a
    right = length - left
    dist = abs(left - right)
    if dist < mdist:
        mdist = dist
        midx = i
ans = mdist
print(ans)
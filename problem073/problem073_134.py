import math
N = int(input())
ans = 0
ve = math.floor(math.sqrt(N))
for st in range(ve):
    tmp = math.floor(N/(st+1)-0.000001)
    score = 2*(tmp - st)
    if score > 0:
        score -= 1
    ans += score
print(ans)
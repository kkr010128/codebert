from collections import Counter

N = int(input())
C = list(input())

cnt = Counter(C)
ans1 = min(cnt["R"], cnt["W"])

ans2 = 0
l, r = 0, N-1
while l < r:
    if C[l] == "W" and C[r] == "R":
        ans2 += 1
        l += 1
        r -= 1
    else:
        if C[l] == "R":
            l += 1
        if C[r] == "W":
            r -= 1

ans = min(ans1, ans2)
print(ans)



N, *A = map(int, open(0).read().split())
X = [(x-l, x+l) for x, l in zip(*[iter(A)]*2)]
X.sort()
ans = 1
L, R = X[0]
for l, r in X[1:]:
    if R <= l:
        ans += 1
        L = l
        R = r
    elif R > r:
        R = r
print(ans)

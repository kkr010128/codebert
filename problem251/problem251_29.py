import collections
n, k = [int(w) for w in input().split()]
r, s, p = [int(w) for w in input().split()]
score = {"s": r, "p": s, "r": p}

t = input()

cnt = collections.Counter(t)

ans = 0
ans += cnt["s"] * r
ans += cnt["p"] * s
ans += cnt["r"]*p

for i in range(k):
    sp_t = t[i:n: k]
    is_prev_lose = False
    for j in range(1, len(sp_t)):
        if sp_t[j - 1] == sp_t[j]:
            if is_prev_lose:
                is_prev_lose = False
            else:
                is_prev_lose = True
                ans -= score[sp_t[j]]
        else:
            is_prev_lose = False
print(ans)

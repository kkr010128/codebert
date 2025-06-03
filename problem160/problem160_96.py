from itertools import combinations_with_replacement
n, m, q = map(int, input().split())
list_ABCD = [ list(map(int,input().split(" "))) for _ in range(q)]
list_N = [i for i in range(1, m+1)]
ans = 0

for l in combinations_with_replacement(list_N, n):
    score = 0
    for a, b, c, d in list_ABCD:
        if l[b-1] - l[a-1] == c:
            score += d
    ans = max(ans, score)

print(ans)
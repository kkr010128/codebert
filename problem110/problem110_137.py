from itertools import combinations
import copy

H, W, K = map(int, input().split())
C = [list(input()) for _ in range(H)]
ans = 0

w = list(range(W))
h = list(range(H))
for i in range(W+1):
    for comi in combinations(w, i):
        for j in range(H+1):
            for comj in combinations(h, j):
                tmpC = copy.deepcopy(C)
                for ci in comi:
                    for hj in range(H):
                        tmpC[hj][ci] = '.'
                for cj in comj:
                    for wi in range(W):
                        tmpC[cj][wi] = '.'
                tmp = 0
                for tc in tmpC:
                    tmp += tc.count('#')
                if tmp == K:
                    ans += 1

print(ans)
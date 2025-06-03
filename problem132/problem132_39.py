from itertools import accumulate
import sys
N, K = map(int, input().split())
An = list(map(int, input().split()))

for cnt in range(K):
    tmp = [0]*(N+1)
    for i in range(N):
        power = An[i]
        left = max(0, i-power)
        right = min(N, i+power+1)
        tmp[left] += 1
        tmp[right] -= 1
    An = list(accumulate(tmp))[:-1]
    if cnt > 40:
        An = [N]*N
        print(*An)
        sys.exit()
print(*An)

N = int(input())
d = list(map(int, input().split()))

import itertools

ans = 0
pairs = list(itertools.combinations(d, 2))

for pair in pairs:
    ans += pair[0] * pair[1]
    
print(ans)
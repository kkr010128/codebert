from collections import defaultdict
N = int(input())
As = list(map(int, input().split()))

l_count = defaultdict(int)
r_count = defaultdict(int)
for i, A in enumerate(As):
    l_count[i + A] += 1
    r_count[i - A] += 1
    
ans = 0
for k, lv in l_count.items():
    rv = r_count[k]
    ans += lv * rv

print(ans)
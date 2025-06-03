from itertools import combinations
n = int(input())
L = list(map(int,input().split()))
ans = 0
for a,b,c in combinations(L,3):
    ans += (2*max(a,b,c) < a+b+c)*(a != b and b != c and c != a)
print(ans)
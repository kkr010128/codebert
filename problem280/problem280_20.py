import itertools,math
n = int(input())
points = [list(map(int,input().split())) for _ in range(n)]
roots = list(itertools.permutations(points))
ans = 0
for root in roots:
    for i in range(n-1):
        ans += math.sqrt(pow(root[i+1][0] - root[i][0],2) + pow(root[i+1][1] - root[i][1],2))
ans /= len(roots)
print(ans)
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N = int(input())
xs, ys = [], []
for _ in range(N):
    x, y = map(int, input().split())
    x2 = x+y
    y2 = x-y
    xs.append(x2)
    ys.append(y2)

#for i in range(N):
#    print(pts[i])

minX, maxX = min(xs), max(xs)
minY, maxY = min(ys), max(ys)
#print('# minX:', minX, '/ maxX:', maxX, file=sys.stderr)
#print('# minY:', minY, '/ maxY:', maxY, file=sys.stderr)

ans = 0
for x, y in zip(xs, ys):
    cs = [abs(x-minX), abs(x-maxX), abs(y-minY), abs(y-maxY)]
    m = max(cs)
    if m > ans:
        ans = m

print(ans)

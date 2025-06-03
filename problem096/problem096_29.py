import math
N, D = map(int, input().split())
p = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
for x, y in p:
    if D >= math.sqrt(x**2 + y**2):
        cnt += 1
print(cnt)

import math

A, B = map(int, input().split())

volume_A = math.floor(A / 0.08)
volume_B = math.floor(B / 0.1)

min_A, max_A = math.inf, -math.inf
range_A = math.floor(1 / 0.08)
min_B, max_B = math.inf, -math.inf
range_B = math.floor(1 / 0.1)
# print(range_A)
# print(range_B)

for i in range(volume_A - range_A, volume_A + range_A):
    if math.floor(i * 0.08) == A:
        min_A = min(min_A, i)
        max_A = max(max_A, i)

for j in range(volume_B - range_B, volume_B + range_B):
    if math.floor(j * 0.1) == B:
        min_B = min(min_B, j)
        max_B = max(max_B, j)

ans_A = set()
for i in range(min_A, max_A + 1):
    ans_A.add(i)
# print(ans_A)

ans_B = set()
for j in range(min_B, max_B + 1):
    ans_B.add(j)
# print(ans_B)

ans = ans_A & ans_B

if len(ans) == 0:
    print(-1)
else:
    print(min(ans))

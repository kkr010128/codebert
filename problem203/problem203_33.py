import math

t8 = [[] for _ in range(130)]
t10 = [[] for _ in range(130)]
for i in range(1251):
    t8[math.floor(i * 0.08)].append(i)
    t10[math.floor(i * 0.1)].append(i)

a, b = map(int, input().split())
if min(t8[a]) > max(t10[b]) or max(t8[a]) < min(t10[b]):
    print(-1)
else:
    print(max(min(t8[a]), min(t10[b])))

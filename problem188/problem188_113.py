X, Y, A, B, C = map(int, input().split())

P = [[] for _ in range(3)]

for p in map(int, input().split()):
    P[0].append((p,0))
for p in map(int, input().split()):
    P[1].append((p,1))
for p in map(int, input().split()):
    P[2].append((p,2))
P[0].sort(reverse=True)
P[1].sort(reverse=True)
P[2].sort()

P[0] = P[0][:X]
P[1] = P[1][:Y]

data = P[0] + P[1]
data.sort(reverse=True)
num = [A,B]
res = sum(map(lambda x: x[0], data))
while True:
    p, i = data.pop()
    q, _ = P[2].pop()
    if p >= q:
        break
    if num[i] - 1 >= 0:
        num[i] -= 1
        res += q - p
    if sum(num) == 0:
        break
    if len(P[2]) == 0:
        break

print(res)

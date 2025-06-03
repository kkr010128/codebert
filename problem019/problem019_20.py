n, q = list(map(int, input().split()))
que = []

for i in range(n):
    p, t = input().split()
    que.append([p, int(t)])

total = 0
while True:
    if q >= que[0][1]:
        total += que[0][1]
        print(que[0][0], total)
        que.pop(0)
    else:
        total += q
        que[0][1] -= q
        que.append(que[0])
        que.pop(0)
    if len(que) == 0:
        break


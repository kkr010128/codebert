X, Y, A, B, C = map(int, input().split(' '))

apples = []
for p in map(int, input().split(' ')):
    apples.append((p, 0))

for q in map(int, input().split(' ')):
    apples.append((q, 1))

for r in map(int, input().split(' ')):
    apples.append((r, 2))

apples.sort(reverse=True)

pq = []
r = []
x = X
y = Y

for d, t in apples:
    if t == 0:
        if x > 0:
            x -= 1
            pq.append(d)
        else:
            continue
    elif t == 1:
        if y > 0:
            y -= 1
            pq.append(d)
        else:
            continue
    else:
        r.append(d)

pq_len = len(pq)
for i in range(len(r)):
    if i >= pq_len:
        break

    if r[i] <= pq[-(i + 1)]:
        break

    pq[-(i + 1)] = r[i]

print(sum(pq))

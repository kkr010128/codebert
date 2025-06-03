X, Y, A, B, C = list(map(int, input().split()))
p = list(map(int, input().split()))
q = list(map(int, input().split()))
r = list(map(int, input().split()))

p.sort()
q.sort()
list.sort(r, reverse=True)

p = p[(A-X):]
q = q[(B-Y):]

i_p = 0
i_q = 0
for i_r in range(C):
    if i_p >= len(p):
        if q[i_q] < r[i_r]:
            q[i_q] = r[i_r]
            i_q += 1
    elif i_q >= len(q):
        if p[i_p] < r[i_r]:
            p[i_p] = r[i_r]
            i_p += 1
    elif p[i_p] <= q[i_q]:
        if p[i_p] < r[i_r]:
            p[i_p] = r[i_r]
            i_p += 1
    else:
        if q[i_q] < r[i_r]:
            q[i_q] = r[i_r]
            i_q += 1

    if i_p >= len(p) and i_q >= len(q):
        break

res = 0

for i in range(len(p)):
    res += p[i]

for i in range(len(q)):
    res += q[i]

print(res)
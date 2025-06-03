x, y, a, b, c = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
r = list(map(int, input().split()))
p.sort(reverse = 1)
p.append(-1)
pc = 0
q.sort(reverse = 1)
q.append(-1)
qc = 0
r.sort(reverse = 1)
r.append(-1)
rc = 0
count = x + y
ans = 0
while count > 0:
    if x > 0 and y > 0:
        if max(p[pc], max(q[qc], r[rc])) == p[pc]:
            ans += p[pc]
            x -= 1
            count -= 1
            pc += 1
        elif max(q[qc], r[rc]) == r[rc]:
            ans += r[rc]
            rc += 1
            count -= 1
        else:
            ans += q[qc]
            qc += 1
            count -= 1
            y -= 1
    elif y > 0:
        if max(q[qc], r[rc]) == r[rc]:
            ans += r[rc]
            rc += 1
            count -= 1
        else:
            ans += q[qc]
            qc += 1
            count -= 1
            y -= 1
    elif x > 0:
        if max(p[pc], r[rc]) == r[rc]:
            ans += r[rc]
            rc += 1
            count -= 1
        else:
            ans += p[pc]
            pc += 1
            count -= 1
            x -= 1
print(ans)
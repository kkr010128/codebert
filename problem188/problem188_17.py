X, Y, A, B, C = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
r = list(map(int, input().split()))
p.sort(reverse=True)
q.sort(reverse=True)
r.sort()

R = p[:X]
G = q[:Y]
i = X - 1
j = Y - 1
con = True
while con and len(r) > 0:
    rr = r.pop()
    if R[i] < G[j]:
        if R[i] < rr:
            R[i] = rr
            i -= 1
            continue
        else:
            con = False
    else:
        if G[j] < rr:
            G[j] = rr
            j -= 1
            continue
        else:
            con = False

print(sum(R) + sum(G))
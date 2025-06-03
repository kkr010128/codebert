from itertools import accumulate

def max_from_acc(A, b):
    r = -10**9-1
    acc = [0] + list(accumulate(A + A[:b]))
    for i in range(len(A)):
        for j in range(1, b+1):
            r = max(r, acc[i+j]-acc[i])
    return r

n, k = map(int, input().split())
P = list(map(int, input().split()))
C = list(map(int, input().split()))

P = [p - 1 for p in P]

checked = [False] * n
loops = []
for i in range(n):
    if checked[i]:
        continue
    checked[i] = True
    tmp = [i]
    next = P[i]
    while next != i:
        tmp.append(next)
        checked[next] = True
        next = P[next]
    loops.append(tmp)

# print(loops)

ans = -10**9-1
for loop in loops:
    t =len(loop)
    div, mod = divmod(k, t)
    if mod == 0:
        mod = t
        div -= 1
    C_loop = [C[p] for p in loop]
    loop_score = sum(C_loop)

    if t >=k:
        ans = max(ans, max_from_acc(C_loop, k))
    else:
        if loop_score > 0:
            ans = max(ans, max_from_acc(C_loop, mod)+loop_score*div)
        else:
            ans = max(ans, max_from_acc(C_loop, t))

print(ans)
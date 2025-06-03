N, K = map(int, input().split())
A = tuple(int(x) - 1 for x in input().split())

done = {0}
rt = [0]
loop_point = 0
while True:
    p = rt[-1]
    np = A[p]
    if np in done:
        loop_point = np
        break
    done.add(np)
    rt.append(np)
if K < len(rt):
    ans = rt[K] + 1
else:
    K -= len(rt)
    rt = rt[rt.index(loop_point):]
    ans = rt[K%len(rt)] + 1
print(ans)
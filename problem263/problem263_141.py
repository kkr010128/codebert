def cin():
    in_ = list(map(int,input().split()))
    if len(in_) == 1:  return in_[0]
    else:  return in_

N = cin()
A = cin()
INF = 10 ** 9 + 7

res = [0 for _ in range(65)]
for i in range(65):
    c0, c1 = 0, 0
    for j in range(N):
        if bool(A[j] & (1 << i)):  c1 += 1
        else:  c0 += 1
    res[i] = c0 * c1
ans = 0
for i in range(65):  ans = (ans + (1 << i) * res[i]) % INF
print(ans)
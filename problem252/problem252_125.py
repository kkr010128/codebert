import bisect

N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
B = [0] * N
B[-1] = A[-1]
for i in range(N - 2, -1, -1):
    B[i] = B[i+1]+A[i]


def C(mid):
    tmp = 0
    for a in A:
        pos = bisect.bisect_right(A, mid - a)
        tmp += N-pos
    return tmp > M


lb = 0
rb = 10**6
while rb - lb > 1:
    happy = (lb + rb) // 2
    if C(happy):
        lb = happy
    else:
        rb = happy

ans = 0
cnt = 0
for a in A:
    pos = bisect.bisect_right(A, rb - a)
    if pos == N:
        continue
    ans += B[pos]+(N-pos)*a
    cnt += N - pos
ans += (M-cnt)*rb
print(ans)

import sys
input = sys.stdin.buffer.readline
N, K = map(int, input().split())
A = [-1] + list(map(int, input().split()))

I = [-1] * (N + 1)
S = []
idx = 1
while I[idx] == -1:
    S.append(idx)
    I[idx] = len(S)
    idx = A[idx]
# print(f'{S=}, {idx=}, {I[idx]=}')

start_idx = I[idx] - 1
num_circles = len(S) - start_idx
# print(f'{start_idx=}, {num_circles=}')

if K < len(S) - 1:
    ans = S[K]
else:
    K -= start_idx
    div, mod = divmod(K, num_circles)
    ans = S[start_idx + mod]
print(ans)

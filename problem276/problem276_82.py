import sys

N = int(input())
A = list(map(int, sys.stdin.readline().rsplit()))
S = [0] * (N + 1)
s = sum(A)

for i in range(N):
    S[i + 1] += S[i] + A[i]

mini = 10 ** 18
for i in range(1, N + 1):
    mini = min(mini, abs(S[N] - 2 * S[i]))

print(mini)

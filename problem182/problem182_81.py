N, K, C = map(int, input().split())
S = [1 if a == "o" else 0 for a in input()]

c = 0
X = [0] * N
Y = [0] * N

i = 0
while i < N:
    if S[i]:
        c += 1
        X[i] = 1
        i += C + 1
    else:
        i += 1

if c > K:
    exit()

i = N - 1
while i >= 0:
    if S[i]:
        Y[i] = 1
        i -= C + 1
    else:
        i -= 1

for i in range(N):
    if X[i] and Y[i]:
        print(i + 1)
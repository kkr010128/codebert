N, K, C = map(int, input().split())
S = input()
mae = [0] * (2 * N)
ato = [0] * (2 * N)

cnt = 0
n = 0 - N - 100

for i in range(N):
    if i - n <= C:
        continue

    if S[i] == 'o':
        mae[cnt] = i
        cnt += 1
        n = i

cnt = K - 1
n = 2 * N + 100

for i in range(N-1, -1, -1):
    if n - i <= C:
        continue

    if S[i] == 'o':
        ato[cnt] = i
        cnt -= 1
        n = i

for i in range(K):
    if mae[i] == ato[i]:
        print(mae[i]+1)

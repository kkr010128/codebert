import sys
input = sys.stdin.readline
n, k = map(int,input().split())
A = list(map(int,input().split()))

S = [A[0] % k]
for i in range(1, n):
    S.append((A[i]+S[-1]) % k)

# print(S)

D = {}
S = [0] + S
ans = 0
for i in range(len(S)):
    key = (S[i] - i) % k

    if i >= k:
        j = i-k
        key1 = (S[j] - j) % k
        D[key1] -= 1
        try:
            ans += D[key1]
            # print(i, j, D[key1])
        except:
            ans += 0

    try:
        D[key] += 1
    except:
        D[key] = 1

for j in range(max(0, len(S)-k), len(S)):
    key1 = (S[j] - j) % k
    D[key1] -= 1
    try:
        ans += D[key1]
        # print(i, j, D[key1])
    except:
        ans += 0
# print(D)
print(ans)
N = int(input())
S = [[] for i in range(N)]
for i in range(N):
    S[i] = input()

S = set(S)
ans = len(S)
print(ans)
S = input()
T = input()
ans = 1000000
for i in range(len(S)-len(T)+1):
    U = S[i:i + len(T)]
    score = 0
    for j in range(len(T)):
        if U[j] != T[j]:
            score += 1
    ans = min(ans, score)

print(ans)

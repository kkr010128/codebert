S = input()
T = input()
ans = 1001
for i in range(len(S)-len(T)+1):
  ans = min(ans, sum(S[i+j] != T[j] for j in range(len(T))))
print(ans)
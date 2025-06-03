import math

S = input()
ans = 0
l = int(math.floor(len(S)/2))
for i in range(l):
    if S[i] != S[len(S)-1-i]:
        ans += 1
print(ans)
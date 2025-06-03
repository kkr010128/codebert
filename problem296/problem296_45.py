import math
S = list(input())
K = int(input())
s = S * 2
c1 = 0
c2 = 0
for i in range(len(s)-1):
    if s[i+1] == s[i]:
        if i < len(S)-1:
            c1 += 1
        c2 += 1
        s[i+1] = 0
c = S[0]
for s in S:
    if s != c:
        print(c1+(c2-c1)*(K-1))
        exit()
print(math.floor(len(S)*K/2))

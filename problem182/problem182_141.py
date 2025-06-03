N, K, C = map(int, input().split())
S = input()
L, R = [], []

i = 0
while len(L) < K:
    if S[i] == "o":
        L.append(i)
        i += C+1
    else:
        i += 1
        
i = N-1
while len(R) < K:
    if S[i] == "o":
        R.append(i)
        i -= C+1
    else:
        i -= 1
        
R = R[::-1]
for i in range(K):
    if L[i] == R[i]:
        print (L[i]+1)
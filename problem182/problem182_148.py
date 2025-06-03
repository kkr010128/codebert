N, K, C = map(int, input().split())
S = input()

L = []
R = []

count_L = C
count_R = C

for i in range(N):
    if S[i] == "o" and count_L >= C:
        count_L = 0
        L.append(i)
    else:
        count_L += 1
        
    if S[N-i-1] == "o" and count_R >= C:
        count_R = 0
        R.append(N-i-1)
    else:
        count_R += 1
        
    if len(L) >= K and len(R) >= K:
        break
    
for l, r in zip(L, R[::-1]):
    if l == r:
        print(l+1)
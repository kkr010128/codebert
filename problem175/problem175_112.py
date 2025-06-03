from collections import Counter
N = int(input())
S = list(input())
cnt = Counter(S)
Red, Green, Blue = (cnt['R'], cnt['G'], cnt['B'])
patn = Red*Green*Blue

cnt = 0
for i in range(N):
    for j in range(i+1, N):
        if (2*j - i) >= N:
            break
        elif S[i] != S[j] and S[j] != S[2*j-i] and S[i] != S[2*j-i]:
            cnt += 1
        
print(patn-cnt)
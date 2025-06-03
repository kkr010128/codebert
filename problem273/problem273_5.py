N,K = map(int, input().split())
A = list(map(int, input().split()))
S = [0 for i in range(N+1)]
for i in range(1,N+1):
    S[i] = S[i-1] + A[i-1]
cnt = 0
dict1 = {}
        
dict1[0] = 1

for j in range(1,N+1):
    if j-K >= 0:
        dict1[(S[j-K]-j+K)%K] -= 1
    if (S[j]-j)%K in dict1:
        cnt += dict1[(S[j]-j)%K]
        dict1[(S[j]-j)%K] += 1
    else:
        dict1[(S[j]-j)%K] = 1
print (cnt)
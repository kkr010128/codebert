#B問題

N = int(input())
A = list(map(int, input().split()))
ans = 0

for i in range(0,len(A)):
    for j in range(i+1,len(A)):
        for k in range(j+1,len(A)):
            if A[i] + A[j] > A[k] and A[j] + A[k] > A[i] and A[k] + A[i] > A[j] and A[i] != A[j] and A[j] != A[k] and A[k] != A[i] :
                ans += 1
print(ans)
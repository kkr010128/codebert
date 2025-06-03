
# D Road to Millionaire
N = int(input())
A = list(map(int, input().split()))
i = 0
M =1000
while i in range(N - 1):
    if A[i] >= A[i+1]:
        i = i + 1   
    else:
        m = (A[i+1] - A[i]) * (M // A[i])
        M = M + int(m)
        i = i + 1
print(M)
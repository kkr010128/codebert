N = int(input())
A = list(map(int, input().split()))

Stock = 0
Money = 1000
 
for i in range(N-1):
    if A[i] < A[i + 1]:

        Stock = Money // A[i]
        Money %= A[i]
        Money += Stock * A[i+1]
print(Money)
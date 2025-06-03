N = int(input())
A = list(map(int, input().split()))
ct = 0
for n in range(N + 1):
    if n % 2:
        if A[n - 1] % 2:
            ct +=1 
print(ct)
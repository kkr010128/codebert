N = int(input())
A = list(map(int,input().split()))
if 0 in A:
    prod = 0
else:
    prod = 1
    for i in range(N):
        prod *= A[i]
        if prod>10**18:
            prod = -1
            break
print(prod)
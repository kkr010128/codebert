n = int(input())
A = list(map(int,input().split()))
L = [0] * n
for i in A:
    L[i - 1] += 1
for j in L:
    print(j)
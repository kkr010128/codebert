N = int(input())
A = [int(i) for i in input().split(" ")]
Min = float("inf")
index = 0
L = 0
R = sum(A)
for i in range(0,len(A)):
    L+=A[i]
    R-=A[i]
    diff = abs(L - R)
    if diff < Min:
        Min = diff
print(Min)
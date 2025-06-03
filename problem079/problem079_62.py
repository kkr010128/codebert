s=int(input())
A=[0,0,1]
for i in range(3,s):
    A+=[A[i-1]+A[i-3]]

print(A[s-1]%(10**9+7))
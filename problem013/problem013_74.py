#ALDS1_1_D Maximum Profit
n=int(input())
A=[]
max_dif=-1*10**9
for i in range(n):
    A.append(int(input()))
min=A[0]
for i in range(n-1):
    if(A[i+1]-min>max_dif):
        max_dif=A[i+1]-min
    if(min>A[i+1]):
        min=A[i+1]
print(max_dif)
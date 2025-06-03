#ALDS_1_1_D Maximum Profit

N=int(input())
A=[]
for i in range(N):
    A.append(int(input())) 
MIN= A[0]
MAX= A[1]-A[0]
for i in range(1,N):
    MAX=max(MAX,A[i]-MIN)
    MIN=min(MIN,A[i])
print(MAX)

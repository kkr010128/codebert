a = input()
N = int(a)
A = list(map(int,input().split()))

flag = 0
y = 1000

for i in range(1,N):
    if A[i-1] < A[i] and flag == 0:
        x = y//A[i-1]
        y = y % A[i-1]
        flag = 1
    if (A[i-1] > A[i]) and flag == 1:
        y = y + A[i-1]*x
        flag = 0
    if flag == 1 and i == N-1:
        y = y + A[i]*x

print(y)
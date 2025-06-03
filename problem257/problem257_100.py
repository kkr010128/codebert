N = int(input())
A = list(map(int, input().split()))
j=0
for i in range(N):
    if A[i]==j+1:
        j+=1

if j == 0:
    print(-1)
else:
    print(N-j)
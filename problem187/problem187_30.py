N,X,Y = (int(x) for x in input().split())
A = [0]*(N)

for i in range(1,N):
    for j in range(i+1,N+1):
        if j <= X or i >= Y:
            A[j-i] += 1
        else:
            A[min((j-i),(abs(i-X)+abs(j-Y)+1))] += 1

for i in range(1,N):
    print(A[i])

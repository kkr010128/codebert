N,X,Y =map(int,input().split())

count = [0] * (N-1)


for i in range(1,N):
    path = abs(X-i) +1
    for j in range(i+1,N+1):
        dist = min(j-i, path+abs(Y-j))
        count[dist-1] +=1


print(*count, sep="\n")
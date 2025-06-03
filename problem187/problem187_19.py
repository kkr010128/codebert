N,X,Y =map(int,input().split())

count = [0] * (N-1)


for i in range(1,N):
    for j in range(i+1,N+1):
        dist = min(j-i, abs(X-i)+1+abs(Y-j))
        count[dist-1] +=1


print("\n".join(map(str,count)))
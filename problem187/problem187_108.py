import sys

N,X,Y = map(int, input().split())

d = [0]*(N-1)

for i in range(N-1):
    for j in range(i+1,N):
        d[min(j-i,abs((X-1)-i)+1+abs((Y-1)-j))-1] += 1
        #print(i,j,min(j-i,abs((X-1)-i)+1+abs((Y-1)-j))-1)

for i in range(len(d)):
    print(d[i])
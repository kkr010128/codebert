K,N=map(int,input().split())
lis=list(map(int,input().split()))

dt=[lis[i+1]-lis[i] for i in range(N-1)]+[lis[0]+(K-lis[-1])]
print(K-max(dt))
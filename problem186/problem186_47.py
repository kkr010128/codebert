K,N=map(int,input().split())
Alist=list(map(int,input().split()))
Alist+=[Alist[0]+K]
diflist=[Alist[i+1]-Alist[i] for i in range(N)]
print(K-max(diflist))
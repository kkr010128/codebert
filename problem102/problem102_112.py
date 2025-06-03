N,K = map(int,input().split())
a = list(map(int,input().split()))
for i in range(1,N-K+1):
    if a[K+i-1]>a[i-1]:
        print("Yes")
    else:
        print("No")
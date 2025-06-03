isPrime=[1 for i in range(10**6+1)]
isPrime[0]=0;isPrime[1]=0
for i in range(2,10**6+1):
    if isPrime[i]==0:
        continue
    for j in range(2*i,10**6+1,i):
        isPrime[j]=0
X=int(input())
for i in range(X,10**6+1):
    if isPrime[i]==1:
        print(i)
        exit()

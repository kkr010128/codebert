N=int(input())
X=input()
def calc(n,count):
    if n==0:
        return count
    popcount=bin(n).count("1")
    next_n=n%popcount
    #print(next_n)
    if next_n==0:
        return count+1
    else:
        return calc(next_n, count+1)

popcount=X.count("1")
if popcount==1:
    plus=0
    for i in range(N):
        x=X[i]
        if x=="1":
            plus+=pow(2,N-i-1,popcount+1)
    for i in range(N):
        x=X[i]
        if x=="1":
            print(0)
        else:
            ans=plus+pow(2,N-i-1,popcount+1)
            ans%=(popcount+1)
            print(calc(ans,1))
    exit()


plus=0
minus=0
for i in range(N):
    x=X[i]
    if x=="1":
        plus+=pow(2,N-i-1,popcount+1)
        minus+=pow(2,N-i-1,popcount-1)
        plus%=(popcount+1)
        minus%=(popcount-1)

for i in range(N):
    x=X[i]
    if x=="1":
        ans=minus-pow(2,N-i-1,popcount-1)
        ans%=(popcount-1)
        print(calc(ans,1))

    else:
        ans=plus+pow(2,N-i-1,popcount+1)
        ans%=(popcount+1)
        print(calc(ans,1))

n,k=map(int,input().split())
l=list(map(int,input().split()))
maxi=0
suml=sum(l[:k])
maxl=sum(l[:k])
for i in range(n-k):
    if suml-l[i]+l[k+i]>maxl:
        maxl=suml-l[i]+l[k+i]
        maxi=i+1
    suml=suml-l[i]+l[k+i]
sumsum=0
for j in range(maxi,maxi+k):
    sumsum+=(l[j]+1)/2
print(sumsum)
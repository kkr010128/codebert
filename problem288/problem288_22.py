n=int(input())
#i+j-2=cnt & i*j=n
minn=n+2
i=1
while i**2<=n:
    if n%i==0:
        j=n/i
        minn=min(int(i+j-2),minn)
    i+=1
print(minn)
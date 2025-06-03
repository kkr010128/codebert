n=int(input())
if n==2:
    count=1
else:
    count=2
for i in range(2,int(n**0.5)+1):
    if n%i==0:
        k=n//i
        while k>0:
            if k%i==0:
                k=k//i
            else:
                if k%i==1:
                    count+=1
                break
    elif (n-1)%i==0:
        count+=1
        if i!=(n-1)//i:
            count+=1
print(count)

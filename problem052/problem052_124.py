n=int(input())
 
result=[]
for i in range(1,n+1):
    if i %3==0:
        result.append(i)
    else:
        k=i
        for j in range(1,5):
            if k%10==3:
                result.append(i)
                break
            else:
                k=k//10
        else:
            continue
 
print("",*result)
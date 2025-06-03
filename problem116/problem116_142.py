x=input()
y=input()
lst1=[]
lst1=list(x)
lst2=[]
lst2=list(y)
b=0
ans=0
while(b<len(x)):
    if(not lst1[b]==lst2[b]):
        ans=ans+1
    b+=1
print(ans)
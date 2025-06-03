n=int(input())
a=[int(i) for i in input().split()]
flag=0
for i in range(0,len(a)):
    if(a[i]%2==0 and (a[i]%3==0 or a[i]%5==0)):
        pass
    elif(a[i]%2==0 and (a[i]%3!=0 or a[i]%5!=0)):
        flag=1
        break
if(flag==1):
    print('DENIED')
else:
    print('APPROVED')
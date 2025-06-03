n=int(input())
alist=[]
blist=[]
for i in range(n):
    a,b=map(int,input().split())
    alist.append(a)
    blist.append(b)
alist.sort()
blist.sort()
if n%2==1:
    num1=-1*(n//-2)-1
    print(blist[num1]-alist[num1]+1)
else:
    num1=n//2-1
    num2=num1+1
    print((blist[num2]+blist[num1])-(alist[num2]+alist[num1])+1)

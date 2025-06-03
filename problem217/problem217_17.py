n=int(input())
num=list(map(int,input().split()))

num2=[]
for i in num:
    if i%2==0:
        num2.append(i)
num3=[]        
for j in num2:
    if j%3==0 or j%5==0:
        num3.append(0)
    elif j%3!=0 or j%5!=0:
        num3.append(1)

a=sum(num3)

if a==0:
    print("APPROVED")
elif a!=0:
    print("DENIED")

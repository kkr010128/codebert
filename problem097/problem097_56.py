N=int(input())
num = 7
i=1
a=[]
prir1=1
while i<=N:
    xx=num%N
    if xx==0:
        print(i)
        prir1=0
        break
    num=10*xx+7
    i+=1
if prir1:
    print(-1)
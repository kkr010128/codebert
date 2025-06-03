t1,t2=map(int,input().split())
a1,a2=map(int,input().split())
b1,b2=map(int,input().split())
p=a1-b1
q=a2-b2
if p*t1+q*t2==0:print('infinity');exit()
elif p<0:p,q=-p,-q
#p>0
if p*t1+q*t2>0:print(0)
else:
    a=p*t1
    d=-(a+q*t2)
    print(2*(a//d)+int(not(not a%d)))

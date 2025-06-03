import math
def div(s):
    i=1
    while(i<=math.sqrt(s)):
        if(s%i==0):
            if(s//i==i):
                if(i!=1):
                    if(i in d):
                        return False
                    else:
                        d[i]=1
            else:
                if(i!=1):
                    if(i in d):
                        return False
                    else:
                        d[i]=1
                if(s//i!=1):
                    if(s//i in d):
                        return False
                    else:
                        d[s//i]=1
        i+=1
    #print(d,s)
    return True
                

n=int(input())
l=list(map(int,input().split()))

d=dict()

setwise=False
pairWise=True
pairWise&=div(l[0])
pairWise&=div(l[1])
val=math.gcd(l[0],l[1])

for i in range(2,n):
    pairWise&=div(l[i])
    val=math.gcd(val,l[i])
if(pairWise):
    print('pairwise coprime')
elif(val==1):
    print('setwise coprime')
else:
    print('not coprime')

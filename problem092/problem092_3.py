x,k,d=map(int,input().split())
x=abs(x) 

if x%d==0:
    minNear  = x%d + d
    minFar = x%d
    minTransitionToNear = (x-minNear)/d
    #print(minNear)
    #print(minFar)
    #print(minTransitionToNear)
    
else:
    minNear  = x%d
    minFar = x%d - d
    minTransitionToNear = (x-minNear)/d
    #print(minNear)
    #print(minFar)
    #print(minTransitionToNear)
    
if k<minTransitionToNear:
    print(x-k*d)
else:
    if (k-minTransitionToNear)%2==0:
        print(abs(minNear))
    else:
        print(abs(minFar))
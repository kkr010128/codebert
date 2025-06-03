import sys 
x,y,A,B,C=map(int,sys.stdin.readline().split())
R=list(map(int,sys.stdin.readline().split()))
G=list(map(int,sys.stdin.readline().split()))
N=list(map(int,sys.stdin.readline().split()))
arr=[]
for i in range(A):
    arr.append([R[i],-1])
for i in range(B):
    arr.append([G[i],-2]) 
for i in range(C):
    arr.append([N[i],-3])    
arr.sort(reverse=True)
ans=0
adv=0
for i in range(len(arr)):
    if x+y==adv:
        break
    if arr[i][1]==-1:
        if x>0:
            ans+=arr[i][0]
            x-=1 
    elif arr[i][1]==-2:
        if y>0:    
            ans+=arr[i][0]
            y-=1
    else:
        ans+=arr[i][0]
        adv+=1 
        
print(ans)        
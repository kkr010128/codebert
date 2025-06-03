n = int(input())
A = list(map(int, input().split()))
if n==0:
    print(1 if A[0] == 1 else -1)
    exit()
if A[0]!=0:
    print(-1)
    exit()
node1=[0]*(n+1)
node1[0]=1
node2=[0]*(n+1)
node2[0]=1
node2[-1]=A[-1]
for i in range(n):
    x=(node1[i]-A[i])*2
    node1[i+1]=x

for i in range(n,0,-1):
    x=(node2[i]+A[i-1])
    node2[i-1]=x

ans=[]

for i in range(n+1):
    x=min(node1[i],node2[i])
    if x<A[i]:
        print(-1)
        exit()
    ans.append(x)
print(sum(ans))
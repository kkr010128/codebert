n,k=map(int,input().split())
A=[0]+list(map(int,input().split()))

color=["white" for _ in range(n+1)]
DP,index=[],1

while 1:
    if color[index]=="white":color[index]="gray"
    elif color[index]=="gray":color[index]="black"
    DP.append(A[index])
    index=A[index]
    if color[index]=="black":break

repeat=[]
for i in DP:
    if color[i]=="black":
        repeat.append(i)
        if repeat[0]==i and len(repeat)!=1:
            repeat.pop()
            break
length=len(repeat)
cnt=0
for i in DP:
    if repeat[0]==i:break
    cnt +=1

if k<=cnt+length:
    print(DP[k-1])
else:
    k -=cnt
    k %=length
    print(repeat[k-1])
n=int(input())
cnt=0
Arm=[]
for i in range(n):
    x,l=map(int,input().split())
    Arm.append([x+l,x-l])
Arm.sort()

dis=-float('inf')
for i in range(n):
    if dis<=Arm[i][1]:
        cnt+=1
        dis=Arm[i][0]
print(cnt)

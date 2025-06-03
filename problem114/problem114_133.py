d=int(input())
c=list(map(int,input().split()))
num=[]
for i in range(d):
    num.append(list(map(int,input().split())))
ans=0
num2=[0]*26
for i in range(1,d+1):
    t=int(input())
    num2[t-1]=i
    ans+=num[i-1][t-1]
    for j in range(26):
        ans-=((i-num2[j])*c[j])
    print(ans)

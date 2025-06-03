import sys
input=sys.stdin.readline #文字列入力はするな！！
sys.setrecursionlimit(10**9) #再帰の上限をあげる

n=int(input())
a=list(map(int,input().split()))

z=[0]*(10**6+1)
for i in a:
    z[i]+=1

x=[-1]*(10**6+1) #2以上の自然数に対して最小の素因数を表す
x[0]=0
x[1]=1
i=2
prime=[]
while i<=10**6:
    if x[i]==-1:
        x[i]=i
        prime.append(i)
    for j in prime:
        if i*j>10**6 or j>x[i]:break
        x[j*i]=j
    i+=1

ans=0
for i in a:
    f=0
    u=i
    if z[u]>=2:
        f=1
    w=[[1,0]]
    p=x[u]
    cnt=1
    while u>1:
        if p==x[u//p]:
            cnt+=1
            u=u//p
        else:
            w.append([p,cnt])
            cnt=1
            u=u//p
            p=x[u]
    m=len(w)

    def s(d,y):
        global m
        global i
        global f
        if d==m-1:
            p=y
            if p!=i and z[p]>=1:
                f=1
        else:
            for j in range(w[d+1][1]+1):
                s(d+1,y*(w[d+1][0]**j))

    s(0,1)
    if f==0:
        ans+=1
print(ans)

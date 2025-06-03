n,m=map(int,input().split())
s=list(input())
s.reverse()
ansl=[]
now=0
while now<n:
    f=1
    for i in range(m,0,-1):
        if now+i<n+1 and s[now+i]=="0":
            ansl.append(i)
            now+=i
            f=0
            break
    if f:
        print(-1)
        exit()


ansl.reverse()
print(*ansl)

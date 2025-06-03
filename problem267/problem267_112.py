N=int(input())
#m1,d1=map(int,input().split())
#hl=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]
S=list(input())
d=list('0123456789')
ans=0
for d1 in d:
    for d2 in d:
        for d3 in d:
            v=d1+d2+d3
            i=0
            p=0
            while i < N :
                if v[p]==S[i]:
                    p+=1
                    if p == 3:
                        break
                i+=1
            if p==3 :
                ans+=1
print(ans)
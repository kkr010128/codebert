D = int(input())
cs = list(map(int, input().split()))
ss = [input().split() for l in range(D)]
ts = [int(input()) for i in range(D)]
ans=0
all_cs=sum(cs)
cs_last=[0]*26

def c0(d):
    mainas=0
    for i in range(26):
        #print(cs[i]*(d-cs_last[i]))
        mainas-=cs[i]*(d-cs_last[i])
    return mainas



for i in range(D):
    cs_last[ts[i]-1]=i+1
    ans+=int(ss[i][ts[i]-1])+c0(i+1)
    
    print(ans)
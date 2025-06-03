
def calc_score(sch):
    d=[0]*26
    score=0
    for i in range(dur):
        j=sch[i]-1
        s=S[i]
        score+=s[j]+c[j]*(i+1-d[j])+sum([-c[k]*(i+1-d[k]) for k in range(26)])
        d[j]=i+1
    return score

def greedy(dur,c,S):
    sch=[]
    d=[0]*26
    r=4
    for i in range(dur):
        t=0
        s=S[i]
        m=-1<<64
        for j in range(26):
            alt=s[j]+r*c[j]*(i+1-d[j])+sum([-r*c[k]*(i+1-d[k]) for k in range(26)])
            if alt>m:
                m=alt
                t=j
        sch.append(t+1)
        d[t]=i+1
    return sch

dur=int(input())
c=list(map(int,input().split()))
S=[list(map(int,input().split())) for i in range(dur)]

sch=greedy(dur,c,S)

for i in sch:
    print(i)

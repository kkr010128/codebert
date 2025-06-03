import random,time
def score(D,c,s,t):
    v=list()
    last=[0]*26
    legacy=0
    for i in range(D):
        minus=0
        v.append(legacy)
        v[i]+=s[i][t[i]-1]
        last[t[i]-1]=i+1
        for j in range(26):
            minus+=c[j]*(i+1-last[j])
        v[i]-=minus
        legacy=v[i]
    return v[D-1]
time_sta = time.perf_counter()
s=list()
t=list()
D=int(input())
c=list(map(int,input().split()))
for i in range(D):
    s.append(list(map(int,input().split())))
t=[random.randint(1,26)]*D
time_end=time.perf_counter()
tim=time_end-time_sta
while tim<1.9:
    d=random.randint(1,D)
    q=random.randint(1,26)
    old=t[d-1]
    oldscore=score(D,c,s,t)
    t[d-1]=q
    if score(D,c,s,t)<oldscore:
        t[d-1]=old
    time_end=time.perf_counter()
    tim=time_end-time_sta
for i in range(D):
    print(t[i])
D=int(input())
c=[]
c=list(map(int,input().split()))
s=[]
for i in range(D):
    s.append(list(map(int,input().split())))


t=[0 for i in range(D)]
for i in range(D):
    t[i]=int(input())






wa=0

last=[0 for i in range(26)]

for i in range(D):
    wa=s[i][t[i]-1]+wa
    last[t[i]-1]=i+1

    for j in range(26):
        wa=wa-c[j]*((i+1)-last[j])
    print(wa)

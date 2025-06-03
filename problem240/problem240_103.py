n,m=map(int,input().split())

AC=[0]*n
WA=[0]*n

for i in range(m):
    t=input().split()
    p, s= int(t[0]), t[1]
    if s=='AC':
        AC[p-1]=1
    elif s=='WA' and AC[p-1]==0:
        WA[p-1]+=1

ac, wa=0,0

for i in range(n):
    if AC[i]:
        ac+=1
        wa+=WA[i]

print(ac, wa)
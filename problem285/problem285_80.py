S = input()
N=len(S)+1
SS = '>'+S+'<'
a = [-1]*(N+2)
for i in range(N+1):
    if SS[i] == '>' and SS[i+1]=='<':
        a[i+1]=0
b = a[1:-1]
c = a[1:-1]

for i in range(N-1):
    if S[i] == '<' and b[i]>=0 :
        b[i+1] = b[i] +1


for i in range(N-2,-1,-1):
    if S[i] == '>' and c[i+1]>=0:
        c[i] = c[i+1] +1

ans = 0
for bb,cc in zip(b,c):
    ans += max(bb,cc) 

print(ans)


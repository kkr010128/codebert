S=input()
T=input()
Slen=len(S)
Tlen=len(T)
ans=5000
for i in range(0,Slen-Tlen+1):
    tans=0
    for j in range(0,Tlen):
        if S[i+j]!=T[j]:
            tans+=1
    if tans<ans:
        ans=tans
print(ans)

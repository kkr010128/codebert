T=input()
N=len(T)

l=[]
for i in range(N):
    if T[i]=="?":
        l.append("D")
    else:
        l.append(T[i])

ans=""
for i in range(N):
    ans+=l[i]

print(ans)
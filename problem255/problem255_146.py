N=int(input())
S,T=map(list,input().split())
U=[]
for i in range(N):
    U.append("")
for i in range(N):
    U[i]=S[i]+T[i]
print(''.join(U))
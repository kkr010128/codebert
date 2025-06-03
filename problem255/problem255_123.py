N=int(input())
S,T=map(list,input().split())
lis=[]
for i in range(0,N):
  lis.append(S[i])
  lis.append(T[i])
print(''.join(lis))
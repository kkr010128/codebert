N=int(input())
S,T=input().split()
list=[]
for i in range(N):
    list.append(S[i]+T[i])
print(''.join(list))


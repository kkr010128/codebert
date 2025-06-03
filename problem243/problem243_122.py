N=int(input())
S=['A']*N
T=[0]*N
for i in range(N):
    s,t=input().split()
    S[i]=s
    T[i]=int(t)
print(sum(T[S.index(input())+1:]))
N=int(input())
s,t=[],[]
for i in range(N):
    S,T=input().split()
    s.append(S)
    t.append(int(T))
X=input()
xs=s.index(X)
print(sum(t[xs:])-t[xs])
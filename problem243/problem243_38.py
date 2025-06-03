N=int(input())
s=[]
t=[]
for i in range(N):
    x,y=input().split()
    s.append(x)
    t.append(int(y))
X=input()

begin_idx=s.index(X)+1

print(sum(t[begin_idx:]))

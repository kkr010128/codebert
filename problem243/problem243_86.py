N=int(input())
music=[]
T=[]
ans=0
for i in range(N):
    s, t=input().split()
    t=int(t)
    music.append(s)
    T.append(t)
X=input()
num=music.index(X)
for j in range(num+1, N):
    ans+=T[j]
print(ans)
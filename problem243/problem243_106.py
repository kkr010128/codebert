N=int(input())
S=[]
T=[]
total=0
for i in range(N):
    s,t=map(str,input().split())
    t=int(t)
    total+=t
    S.append(s)
    T.append(t)
X=input()
flag=True
a=0
j=0
while flag:
    a+=T[j]
    if S[j]==X:
        flag=False
    j+=1
print(total-a)
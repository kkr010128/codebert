N,K=map(int,input().split())
R,S,P=map(int,input().split())
L=input()
T=[]
for i in range(N):
    T.append(L[i])
for i in range(K,N):
    if T[i]==T[i-K]:
        T[i]="0"
p=0
for i in T:
    if i=="r":
        p+=P
    elif i=="s":
        p+=R
    elif i=="p":
        p+=S
print(p)
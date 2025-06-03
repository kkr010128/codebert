S=int(input())
T=list(input())
t=S//2
p=0
for i in range(t):
    if S%2==1:
        p=-1
        break
    elif T[i]!=T[i+t]:
        p=-1
        break
if p==-1 or t==0:
    print("No")
elif p==0:
    print("Yes")
    


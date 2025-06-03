n=int(input())

T=0
H=0

for i in range(n):
    t,h=list(input().split())
    if t==h:
        T+=1
        H+=1
    elif t>h:
        T+=3
    elif t<h:
        H+=3
        
print(T,H)
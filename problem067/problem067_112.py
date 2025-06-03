n=int(input())
H=[]
T=[]
for i in range (n):
    a=list(map(str, input().split())) 
    if a[0]>a[1] :
        H.append(3)
    elif a[0]<a[1] :
        T.append(3)
    else :
        H.append(1)
        T.append(1)
        

print(sum(H), sum(T))

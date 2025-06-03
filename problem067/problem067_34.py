n=int(input())

A=0
B=0
for i in range(n):    
    a,b=map(str,input().split())
    if a>b:
        A+=3
    elif a==b:
        A+=1
        B+=1
    elif a<b:
        B+=3
print(A,B)
        

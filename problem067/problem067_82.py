n=int(input())
t=0
h=0
for i in range(n):
    a,b=map(str,input().split())
    if a<b:
        h+=3
    
    elif a>b:
        t+=3
    else:
        t+=1
        h+=1
print("{} {}".format(t,h))
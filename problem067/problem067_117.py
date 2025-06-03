n=input()
t=h=0
for i in range(n):
    x,y=map(str,raw_input().split())
    if x==y:
        t+=1
        h+=1
    elif x<y:
        h+=3
    else:
        t+=3
print t,h
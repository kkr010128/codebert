t,h=0,0
n=int(input())
for i in range(n):
    a,b=input().split()
    if a > b:
        t+=3
    elif a < b:
        h+=3
    else:
         t+=1
         h+=1
print(t, h)
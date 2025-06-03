n=int(input())
s,t=map(str,input().split())
a=""
for i in range(2*n):
    if i%2==0:
        a=a+s[(i)//2]
    else:
        a=a+t[(i-1)//2]
print (a)
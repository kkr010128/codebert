a,b=map(int,input().split())
for i in range(1,a+1):
    if b*i%a==0:
        print(b*i)
        break
a,b=map(int,input().split())
num=1
while 1:
    if int(num*0.08)==a and int(num*0.1)==b:
        print(num)
        break
    if int(num*0.08)>a and int(num*0.1)>b:
        print(-1)
        break
    num+=1
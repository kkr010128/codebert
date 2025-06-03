k=int(input())
a,b=map(int,input().split())
flag=0
for i in range(1001):
    if a<=k*i<=b:
        print("OK")
        flag+=1
        break

if flag==0:
    print("NG")
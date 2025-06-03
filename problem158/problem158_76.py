k=int(input())
a,b=map(int,input().split())
c=1
for i in range(a,b+1):
    if i%k==0:
        print("OK")
        c=0
        break
if c==1:
    print("NG")

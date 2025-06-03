k=int(input())
a,b=map(int,input().split())
cnt=0
for i in range(a, b+1):
    if i%k==0:
        cnt+=1
if cnt>0:
    print('OK')
else :
    print('NG')

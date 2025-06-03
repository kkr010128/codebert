n=int(input())
a=list(map(int,input().split()))
ct=0
for i in range(n):
    if a[i]==(ct+1):
        ct+=1
if ct==0:
    print('-1')
else:
    print(n-ct)
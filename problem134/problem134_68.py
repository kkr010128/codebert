n=int(input())
l=list(map(int,input().split()))
p=1
l.sort()
for i in l:
    p*=i
    if(p==0):
        print(0)
        exit()
    if(p>10**18):
        print(-1)
        exit()
print(p)
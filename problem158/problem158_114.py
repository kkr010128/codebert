k=int(input())
a,b=map(int,input().split())
ans=False
for i in range(a,b+1):
    if i%k==0:
        ans=True
        break
print("NOGK"[ans::2])
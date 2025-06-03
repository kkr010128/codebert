l,r,d=map(int,input().split())
count=0
for i in range(d,r+1,d):
    if l<=i<=r:
        count+=1
print(count)
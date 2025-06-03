a,b,c=map(int,input().split())
d=[i for i in range(a,b+1)]
count=0
for i in d:
    if c%i==0:
        count+=1
print(count)
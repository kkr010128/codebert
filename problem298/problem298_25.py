n=list(map(int,input().split()))
a=list(map(int,input().split()))
count=0
for i in range(0,len(a)):
    if n[1]<=a[i]:
        count+=1
print(count)
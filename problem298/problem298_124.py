n,k = map(int,input().split())
count=0

l= list(map(int,input().split()))

for i in range(len(l)):
    if l[i]>=k:
        count=count+1

print(count)
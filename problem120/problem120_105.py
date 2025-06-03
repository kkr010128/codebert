a,b=map(int,input().split())
n=list(map(int,input().split()))[:a]
n.sort()
sum=0

for i in range(b):
    sum+=n[i]

print(sum)
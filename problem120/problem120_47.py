a,b=map(int,input().split())

c=list(map(int,input().split()))
c.sort()
# print(c)

sum=0
for i in range(b):
    sum+=c[i]

print(sum)
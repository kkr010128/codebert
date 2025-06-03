

k=map(int, raw_input().split())

a=k[0]
b=k[1]
c=k[2]
count=0

for i in range(a,b+1):
    if c%i==0:
        count=count+1

print count
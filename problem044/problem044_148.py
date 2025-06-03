a,b,c=[int(i) for i in input().split()]

num=0
#s=[i for i in range(1,c+1) if c%i==0]
# print(s)

for i in range(1,c+1):
    if c%i==0:
        if i>=a and i<=b:
            num=num+1
print(num)
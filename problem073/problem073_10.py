n = int(input())
a=1
x=0
for i in range(n-1):
    x += (n-1)//a
    a += 1
print(x)
n=int(input(''))
p=0
for i in range(n-1):
    a=i+1
    p=p+(n-1)//a
print(p)
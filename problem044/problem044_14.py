x, y, z = input().split()
a = int(x)
b = int(y)
c = int(z)

count = 0
num = a
    
while num <= b:
    if c % num == 0:
        count += 1
    else:
        pass
    num += 1
    
print(count)

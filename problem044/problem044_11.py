ABC = input().split()
a = int(ABC[0])
b = int(ABC[1])
c = int(ABC[2])
i = 0
while a<=b:
    if c%a==0:
        i = i+1
    a = a+1
print(i)
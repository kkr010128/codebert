N = input().split()

a = int(N[0])
b = int(N[1])
c = int(N[2])

count = 0
while a <= b:
    if c % a == 0:
       count += 1
    a += 1
print(count)
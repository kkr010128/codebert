#ALDS 1-B: Greatest Common Divisor

x = input().split()
a = int(x[0])
b = int(x[1])

while(a % b != 0):
    c = b
    b = a % b
    a = c
print(b)


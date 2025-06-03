x = list(input().split(" "))
a = int(x[0])
b = int(x[1])
c = int(x[2])
divisors = 0
for i in range(a, b+1):
    if c % i == 0:
        divisors += 1
print(divisors)
n = input()
x = 1
print '',
while True:
    if x > n:
        break
    if (x % 3 == 0) or ('3' in str(x)):
        print x,
    x += 1
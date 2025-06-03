def isPrime(x):
    if x == 2:
        return True
    elif (x < 2) or (x % 2 == 0):
        return False
    else:
        i = 3
        while i <= float(x) ** 0.5:
            if x % i == 0:
                return False
            i += 2
        return True


t = 0
for i in range(int(input())):
    if isPrime(int(input())):
        t += 1
print(t)
def isprime(x):
    if x == 2:
        return True
    elif x < 2 or x%2 == 0:
        return False
    i = 3
    while i <= pow(x,1/2):
        if x%i == 0:
            return False
        i = i + 2
    return True
count = 0
for s in range(int(input())):
    if isprime(int(input())):
        count += 1
print(count)

n = int(input())

def isPrime(x):
    if x < 2:
        return false
    if x == 2:
        return True
    return pow(2, x-1, x) == 1

s = []
for i in range(n):
    s.append(int(input()))

prime = 0
for i in s:
    if isPrime(i):
        prime += 1
print(prime)
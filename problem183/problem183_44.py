from math import sqrt, log


def factor(number):
    i = 2
    s = set()
    while i * i <= number:
        if number % i == 0:
            if i != 2:
                s.add(i)
            if (number // i) != 2:
                s.add(number//i)
        i += 1
    return s


def newFactor(number):
    n = number
    i = 2
    ans = set()
    while i * i <= number:
        if number % i == 0:
            while number % i == 0:
                number //= i
            if number % i == 1:
                ans.add(i)
        number = n
        i += 1
    return ans


n = int(input())
if n == 2:
    print(1)
    exit()
if n == 3:
    print(2)
    exit()
s = set()
s.add(2)
s.add(n-1)
s.add(n)
s = s.union(factor(n-1))
s = s.union(newFactor(n))
print(len(s))

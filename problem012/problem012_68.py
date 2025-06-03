import math


def judge(n):
    if n < 2:
        return False
    i = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            return False
        i += 1
    return True


count = 0
n = int(input())
for i in range(n):
    if judge(int(input())):
        count += 1
print(count)
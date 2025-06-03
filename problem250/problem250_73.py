import math

for n in range(int(input()),100003+1):
    fact = True
    if n % 2 == 0 and n != 2:
        continue

    for div in range(2,math.floor(math.sqrt(n))+1):
        if n % div == 0:
            fact = False
            break

    if fact:
        print(n)
        break
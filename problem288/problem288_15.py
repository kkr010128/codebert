from math import sqrt
 
N = int(input())
 
search_max = int(sqrt(N))
 
min_number = 10**12
for x in range(1, search_max + 1):
    if N % x == 0:
        y = N // x
        if x + y < min_number:
            min_number = x + y
print(min_number-2)
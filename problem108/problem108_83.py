n = int(input())

from math import ceil
change = ceil(n/1000)*1000 - n
print(change)
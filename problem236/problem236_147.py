from math import ceil
H=int(input())
W=int(input())
N=int(input())
print(min(ceil(N/H),ceil(N/W)))
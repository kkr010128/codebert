import sys
import itertools
N = int(input())
array = list(map(int,input().split()))

sum = 0
for I in list(itertools.combinations(array,2)):
    sum += I[0]*I[1]
print(sum)

import math
import itertools

for i in range(int(input())):
    a, b, c = sorted(map(int, input().split()))
    print('YES' if a*a+b*b==c*c else 'NO')
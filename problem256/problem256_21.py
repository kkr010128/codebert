import sys
import math
input = sys.stdin.readline

a, b = list(map(int, input().split()))

print(a * b // math.gcd(a, b))


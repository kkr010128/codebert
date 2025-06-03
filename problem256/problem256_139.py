import sys
input = sys.stdin.readline

a, b = map(int, input().split())
print(abs(a * b) // __import__('math').gcd(a, b))
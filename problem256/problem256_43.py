from fractions import gcd

A, B = map(int, input().split())

print(str((A * B) // gcd(A, B)))
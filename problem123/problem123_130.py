N = int(input())
A = [int(a) for a in input().split()]
xor = 0

for x in A:
    xor ^= x

for v in  A:
    print(xor^v, end=' ')
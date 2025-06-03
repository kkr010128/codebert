import sys
input = sys.stdin.readline

n = int(input())

a = 0

if n % 2 == 1:
    a == 0
else:
    n = n // 2
    k = 5
    while k <= n:
        a += n // k
        k *= 5

print(a)
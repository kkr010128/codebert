import sys

N = int(input())

result = 0
for a in range(1, N):
    if N % a == 0:
        b_count = N // a - 1
    else:
        b_count = N // a
    result += b_count

print(result)

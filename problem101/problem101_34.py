a, b, c = map(int, input().split())
k = int(input())
while a >= b and k > 0:
    b *= 2
    k -= 1
while b >= c and k > 0:
    c *= 2
    k -= 1
print('Yes' if a < b < c else 'No')
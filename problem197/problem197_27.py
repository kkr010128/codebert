import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
check = c - a - b
if check ** 2 > 4 * a * b and check > 0:
    ans = 'Yes'
else:
    ans = 'No'
print(ans)

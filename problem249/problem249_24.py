a, b, k = map(int, input().split())

if k <= a:
    a -= k
elif a < k <= a + b:
    temp = a
    a = 0
    b -= k - temp
else:
    a = 0
    b = 0
print('{} {}'.format(a, b))
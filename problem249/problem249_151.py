a, b, k = map(int, input().split())
if a >= k:
    a = a - k
else:
    b = b + a - k
    a = 0

if b < 0:
    b = 0
print(str(a) + " " + str(b))

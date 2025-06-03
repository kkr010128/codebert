x = list(map(int, input().split()))

n = x[0]
k = x[1]

y = n % k
if y < abs(y - k):
    print(y)
else:
    print(abs(y - k))
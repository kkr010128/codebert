k, n = map(int, input().split())
a = list(map(int, input().split()))
num = 0
for i in range(n-1):
    x = a[i+1]-a[i]
    num = max(x, num)
f = (k - a[n-1]) + a[0]
if num >= f:
    print(k - num)
else:
    print(k - f)
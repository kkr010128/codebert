n = int(input())
a = list(map(int, input().split()))
kane = 1000
kabu = 0 
if a[0] < a[1]:
    kabu = kane // a[0]
    kane %= a[0]
for i in range(1, n - 1):
    if a[i - 1] < a[i]:
        kane += a[i] * kabu
        kabu = 0
    if a[i] < a[i + 1]:
        kabu = kane // a[i]
        kane %= a[i]
kane += a[n - 1] * kabu
print(kane)
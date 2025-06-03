n, k, s = map(int, input().split())
a = [s] * n
if s == 1:
    s = 2
else:
    s -=1
for i in range(k, n):
    a[i] = s
print(a[0], end = "")
for i in a[1:]:
    print("", i, end = "")
print()

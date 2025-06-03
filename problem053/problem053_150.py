n = int(input())
x = input().split()
a = list(map(int, x))

b = []
for i in range(n):
    b.append(a[n - 1 - i])

for output in b[:n - 1]:
    print(output, end=' ')
print(b[n - 1])


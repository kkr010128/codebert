n = int(input())
x = 100000
for i in range(n):
    x += (x * 0.05 + 999) // 1000 * 1000
print(int(x))
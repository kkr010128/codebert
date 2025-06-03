n = int(input())

i = 1
l = []

while i * i <= n:
    if n % i == 0:
        l.append(i)
    i += 1

a = l[-1]
b = n // l[-1]
ans = a + b - 2
print(ans)
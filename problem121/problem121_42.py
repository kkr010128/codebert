N = int(input())

l = [1]
for i in range(1,12):
    l.append(26**i + l[i-1])
for i in range(12):
    if l[-(i+1)] > N:
        continue
    else:
        order = 12 - i
        break
a = []
for i in range(order):
    a.append(26**i)

n = N - l[order-1]
s = ""
for i in range(order):
    s += ( chr( ord("a") + (n // a[-(i+1)]) ) )
    n -= a[-(i+1)] * (n // a[-(i+1)])

print(s)
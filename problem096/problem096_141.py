n,d = map(int, input().split())
x = []
y = []
for i in range(n):
    a,b = map(int, input().split())
    x.append(a)
    y.append(b)
count = 0
for i in range(n):
    if (x[i]**2 + y[i]**2)**(1/ 2) <= d:
        count += 1
print(count)
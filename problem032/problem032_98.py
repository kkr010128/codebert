n = int(input())
x = [float(s) for s in input().split()]
y = [float(s) for s in input().split()]

xy = [abs(xi-yi) for xi,yi in zip(x,y)]

D = lambda p:sum([xyi**p for xyi in xy])**(1/p)

print(D(1.0))
print(D(2.0))
print(D(3.0))
print(max(xy))
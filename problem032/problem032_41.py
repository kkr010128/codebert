

n = int(input())
X = [int(x) for x in input().split()]
Y = [int(y) for y in input().split()]

d1 = 0
d2 = 0
d3 = 0
Di = []

for i in range(n) :
    d1 += abs(X[i] - Y[i])
print(f"{d1:.6f}")

for i in range(n) :
    d2 += abs(X[i] - Y[i]) ** 2
print(f"{(d2)**(1/2):.6f}")

for i in range(n) :
    d3 += abs(X[i] - Y[i]) ** 3
print(f"{(d3)**(1/3):.6f}")
    
for i in range(n) :
    Di.append(abs(X[i] - Y[i]))
print(f"{max(Di):.6f}")

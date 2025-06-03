n = int(input())
x = list(map(float, input().split()))
y = list(map(float, input().split()))
dif = [abs(i-j) for i, j in zip(x, y)]
print(sum(dif))
print(sum([i**2 for i in dif])**0.5)
print(sum([i**3 for i in dif])**(1/3))
print(max(dif))


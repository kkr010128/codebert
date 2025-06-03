N, D = map(int, input().split())
num = [input().split() for _ in range(N)]
 
X = []
Y = []
count = 0
 
for n in num:
    X.append(int(n[0]))
    Y.append(int(n[1]))
 
for x, y in  zip(X, Y):
    dist = x**2 + y**2
    if dist <= D**2:
        count += 1
 
print(count)
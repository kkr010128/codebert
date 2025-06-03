def dist(X, Y, p):
    return sum(abs(x - y) ** p for x, y in zip(X,Y)) ** (1.0 / p)
    
n = input()
X = map(int, raw_input().split())
Y = map(int, raw_input().split())
for i in [1, 2, 3]:
    print dist(X, Y, i)
print max(map(lambda xy: abs(xy[0] - xy[1]), zip(X, Y)))
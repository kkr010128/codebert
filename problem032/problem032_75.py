from sys import stdin
 
n = int(stdin.readline().rstrip())
x = [float(x) for x in stdin.readline().rstrip().split()]
y = [float(x) for x in stdin.readline().rstrip().split()]
 
def minkowski_dist(x, y, p="INF"):
    if p == "INF":
        return max([abs(x[i]-y[i]) for i in range(n)])
    elif isinstance(p, int):
        return (sum([(abs(x[i]-y[i]))**p for i in range(n)]))**(1/p)
 
print(minkowski_dist(x, y, 1))
print(minkowski_dist(x, y, 2))
print(minkowski_dist(x, y, 3))
print(minkowski_dist(x, y))

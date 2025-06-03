X, Y, R, G, N = map(int, input().split())
r = [int(x) for x in input().split()]
g = [int(x) for x in input().split()]
n = [int(x) for x in input().split()]
r = sorted(r)[R-X:]
g = sorted(g)[G-Y:]

apple = r + g + n
apple = sorted(apple)[len(apple)-(X+Y):]
print(sum(apple))
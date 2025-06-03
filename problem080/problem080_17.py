N = int(input())
xy = [list(map(int, input().split())) for i in range(N)]
z = [x + y for x, y in xy]
w = [x - y for x, y in xy]
print(max(max(z) - min(z), max(w) - min(w)))
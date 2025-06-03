n = int(input())
xy = [list(map(int, input().split())) for _i in range(n)]
x = [i+j for i, j in xy]
y = [i-j for i, j in xy]
x.sort()
y.sort()
print(max(abs(x[0]-x[-1]), abs(y[0]-y[-1])))
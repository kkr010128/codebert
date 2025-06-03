x = list(input().split())
y = list(map(int, input().split()))
z = input()
y[x.index(z)] -= 1
print("{0} {1}".format(y[0], y[1]))

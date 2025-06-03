import math

def hoge(x, y, p):
    s = 0
    for x_i, y_i in zip(x, y):
         s += math.pow(math.fabs(x_i - y_i), p)
    return math.pow(s, 1/p)

_ = input()
x = [int(e) for e in input().split()]
y = [int(e) for e in input().split()]
print (hoge(x, y, 1))
print (hoge(x, y, 2))
print (hoge(x, y, 3))
print (max([math.fabs(x_i - y_i) for x_i, y_i in zip(x,y)]))

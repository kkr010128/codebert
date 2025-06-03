import math
def hoge(a):
    return a * a
x1, y1, x2, y2 = map(float, input().split())
print (math.sqrt(hoge(math.fabs(x1-x2)) + hoge(math.fabs(y1-y2))))

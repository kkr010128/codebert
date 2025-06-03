from collections import namedtuple
import math
Co = namedtuple('Co', 'x y')

def f(i, n, l, r):
    if i >= n:
        return
    il = Co(x=(1/3 * r.x + (1 - 1/3) * l.x), y=(1/3 * r.y + (1 - 1/3) * l.y))
    ir = Co(x=(2/3 * r.x + (1 - 2/3) * l.x), y=(2/3 * r.y + (1 - 2/3) * l.y))

    trix = 1/2 * (ir.x + il.x - math.sqrt(3) * ir.y + math.sqrt(3) * il.y)
    triy = 1/2 * (math.sqrt(3) * ir.x - math.sqrt(3) * il.x + ir.y + il.y)
    trico = Co(trix, triy)

    f(i+1, n, l, il)
    print(il.x, il.y)
    f(i+1, n, il, trico)
    print(trico.x, trico.y)
    f(i+1, n, trico, ir)
    print(ir.x, ir.y)
    f(i+1, n, ir, r)

if __name__ == '__main__':
    n = int(input())
    print(0, 0)
    f(0, n, Co(0,0), Co(100,0))
    print(100, 0)


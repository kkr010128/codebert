import math
N = int(input())
ans = [(0, 0)]
def rec(i, lx, ly, rx, ry):
    if i == N:
        return ans
    else:
        x1 = (2 * lx + rx) / 3
        y1 = (2 * ly + ry) / 3
        x3 = (2 * rx + lx) / 3
        y3 = (2 * ry + ly) / 3
        x2 = (x3 - x1) * math.cos(math.pi/3) \
             - (y3 - y1) * math.sin(math.pi/3) + x1
        y2 = (x3 - x1) * math.sin(math.pi/3) \
             + (y3 - y1) * math.cos(math.pi/3) + y1
        

        rec(i+1, lx, ly, x1, y1)
        ans.append((x1, y1))

        rec(i+1, x1, y1, x2, y2)
        ans.append((x2, y2))

        rec(i+1, x2, y2, x3, y3)
        ans.append((x3, y3))

        rec(i+1, x3, y3, rx, ry)

        return ans
        

answer = rec(0, 0, 0, 100, 0)
answer.append((100, 0))
for pair in answer:
    print(*pair)

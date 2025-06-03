# coding:utf-8

class FLOOR:
    def __init__(self):
        self.room = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

class BUILD:
    def __init__(self):
        self.floor = [FLOOR(), FLOOR(), FLOOR()]

# 3??????10??¨?±????4?£?
all_rooms = [BUILD(), BUILD(), BUILD(), BUILD()]

# ??\???
n = int(input())
for i in range(n):
    b, f, r, v = map(int, input().split())
    all_rooms[b-1].floor[f-1].room[r-1] += v

for b in range(4):
    for f in range(3):
        display = []
        for r in range(10):
            display.append(str(all_rooms[b].floor[f].room[r]))
        print(' ' + ' '.join(display))
    if (b < 3):
        print('#'*20)
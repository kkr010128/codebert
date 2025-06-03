import math

n = int(raw_input())

def func(i, ox1, oy1, ox2, oy2):
    if i != n:
        nx1 = ox1 + (ox2 - ox1) / 3
        ny1 = oy1 + (oy2 - oy1) / 3
        nx2 = ox1 + (ox2 - ox1) * 2 / 3
        ny2 = oy1 + (oy2 - oy1) * 2 / 3
        if nx1 < nx2:
            if ny1 == ny2:
                nx3 = nx1 + (nx2 - nx1) / 2
                ny3 = ny1 + (nx2 - nx1) * math.sqrt(3) / 2
            elif ny1 < ny2:
                nx3 = ox1
                ny3 = ny2
            elif ny1 > ny2:
                nx3 = ox2
                ny3 = ny1
        elif nx1 > nx2:
            if ny1 == ny2:
                nx3 = nx1 + (nx2 - nx1) / 2
                ny3 = ny1 - (nx1 - nx2) * math.sqrt(3) / 2
            elif ny1 < ny2:
                nx3 = ox2
                ny3 = ny1
            elif ny1 > ny2:
                nx3 = ox1
                ny3 = ny2
        func(i+1, ox1, oy1, nx1, ny1)
        func(i+1, nx1, ny1, nx3, ny3)
        func(i+1, nx3, ny3, nx2, ny2)
        func(i+1, nx2, ny2, ox2, oy2)
    elif i == n:
        print(str(ox1) + str(" ") +  str(oy1))

func(0, 0.0, 0.0, 100.0, 0.0)
print(str(100) + str(" ") + str(0))
#!/usr/bin/env python3

import math
x = int(input())

#aもbも0以上のとき
border = 1;
while border ** 5 - (border - 1) ** 5 < x:
    border += 1

for i in range(border + 1):
    aa = ((x + i ** 5) ** (1.0 / 5.0)) #仮
    a = round(aa)
    if a ** 5 - i ** 5 == x:
        b = i
        print(a, b)
        break
else:
    b = -1

    while x + b ** 5 >= 0:

        aa = ((x + b ** 5) ** (1.0 / 5.0))  # 仮
        a = round(aa)
        if a ** 5 - b ** 5 == x:
            print(a, b)
            break
        b -= 1

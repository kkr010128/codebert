# -*- coding: utf-8 -*-

import math


def g(nx, ny, nz):
    return nx ** 2 + ny ** 2 + nz ** 2 + nx * ny + ny * nz + nz * nx


def solve(n):
    # min_z = max(1, int(math.sqrt(n) / 3))
    max_z = max(1, int(math.sqrt(n - 2) - 1) if n > 2 else 1)
    # max_x = max(1, int(math.sqrt(n / 3) + 1))
    
    counter = [0 for _ in range(n + 1)]
    
    for z in range(1, max_z + 1):
        for y in range(1, max_z + 1):
            for x in range(1, max_z + 1):
                gn = g(x, y, z)
                if gn <= n:
                    counter[gn] += 1
    
    for i in range(1, n + 1):
        print(counter[i])


N = int(input())

solve(N)


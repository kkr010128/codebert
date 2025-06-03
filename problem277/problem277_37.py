import numpy as np
inputs = open(0).readlines()

def main(inputs):
    h, w, k = map(int, inputs[0].split())
    cake, count, coords = np.zeros((h, w), dtype=np.uint), 0, {}
    for i, s in enumerate(inputs[1:]):
        for j, c in enumerate(s):
            if c == '#':
                count += 1
                cake[i, j] = count
                coords[count] = (j, i)
    empty_rows = {i for i, rows in enumerate(cake) if not np.any(rows)}

    for i in range(1, count+1):
        x, y = coords[i]
        x0, y0 = x-1, y-1
        x1, y1 = x+1, y+1
        while 0 <= x0 and cake[y, x0] == 0:
            cake[y, x0] = i
            x0 -= 1
        x0 += 1
        while x1 < w and cake[y, x1] == 0:
            cake[y, x1] = i
            x1 += 1
        while 0 <= y0 and y0 in empty_rows:
            cake[y0, x0:x1] = i
            y0 -= 1
        while y1 < h and y1 in empty_rows:
            cake[y1, x0:x1] = i
            y1 += 1

    for rows in cake:
        print(*rows)

main(inputs)
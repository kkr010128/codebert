
danmen = input()
down = []
edge = []
pool = []

for (i, line) in enumerate(danmen):
    if line == "\\":
        down.append(i)
    elif down and line == "/":
        left = down.pop()
        area = i - left

        while edge:
            if edge[-1] > left:
                edge.pop()
                area += pool.pop()
            else:
                break

        edge.append(left)
        pool.append(area)

print(sum(pool))
print(len(pool), *pool)
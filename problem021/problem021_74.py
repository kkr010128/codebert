down = []
edge = []
pool = []
for i,c in enumerate(input()):
    if c == "\\":
        down.append(i)
    elif c == "/" and down:
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
print(" ".join(map(str,[len(pool)]+pool)))


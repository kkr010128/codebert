square = input()
 
down = []
edge = []
pool = []
 
for i, strings in enumerate(square):
    if strings == "\\":
        down.append(i)
    elif down and strings == "/":
        left = down.pop()
        area = i - left
 
        while edge:
            if edge[-1] < left:
                break
            edge.pop()
            area += pool.pop()
 
        edge.append(left)
        pool.append(area)
 
print(sum(pool))
print(len(pool), *pool)
down_positions = []
ponds = []
for index, value in enumerate(raw_input()):
    if value == '\\':
        down_positions.append(index)
    elif value == '/' and down_positions:
        right = index
        left = down_positions.pop()
        area = right - left
        candidate_area = 0
        while ponds and left < ponds[-1][0]:
           candidate_area += ponds.pop(-1)[1]

        ponds.append((left, area + candidate_area))

print sum(x[1] for x in ponds)
print len(ponds), 
for pond in ponds:
    print pond[1], 
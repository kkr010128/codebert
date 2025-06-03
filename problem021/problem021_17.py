lakes = []  # [(左岸位置, 断面積)]
lefts = []  # lefts[i]: まだ対になっていない上から i 番目の左岸位置
for i, c in enumerate(input()):
	if c == '\\':
		lefts.append(i)
	elif c == '/':
		if lefts:
			left = lefts.pop()
			area = i - left
			while lakes:
				sub_left, sub_area = lakes[-1]
				if left < sub_left:
					area += sub_area
					lakes.pop()
				else:
					break
			lakes.append((left, area))

L = [lake[1] for lake in lakes]
print(sum(L))
print(len(L), *L)

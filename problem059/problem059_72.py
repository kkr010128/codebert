y, x = map(int, input().split())
box = []
y_sum = [[]]

for i in range(y):
	box.append(list(map(int, input().split())))
	box[i].append(sum(box[i]))

box_replace = list(map(list, zip(*box)))
[y_sum[0].append(sum(box_replace[i])) for i in range(x+1)]
box += y_sum

[print( " ".join(map(str, box[i])) ) for i in range(y+1)]
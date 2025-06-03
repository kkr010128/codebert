n = int(input())
lst = []

for i in range(n):
	tmp = input().split()
	lst.append(tmp)
	
d = {}

for i in range(n):
	if lst[i][0] == 'insert':
		d[lst[i][1]] = d.get(lst[i][1], 0) + 1
	elif lst[i][0] == 'find':
		print('yes') if lst[i][1] in d else print('no')

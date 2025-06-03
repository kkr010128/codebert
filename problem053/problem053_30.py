n = int(input())
i = 0
list_n = [n]

map_n = map(int, input().split())
list_n = list(map_n)

for value in reversed(list_n):
	print(value, end ='')
	if value != list_n[0]:
		print(' ', end = '')
print()
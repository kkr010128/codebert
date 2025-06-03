n = int(raw_input())
a = map(int, raw_input().split())

def print_list(list):
	for i in range(len(list)-1):
		print(list[i]),
	print(list[len(list)-1])

#print("")
print_list(a)
for i in range(1,n):
	v = a[i]
	j = i - 1
	while j >= 0 and a[j] > v:
		a[j+1] = a[j]
		j -= 1
	a[j+1] = v
	print_list(a)
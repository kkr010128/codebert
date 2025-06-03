ns = list(map(int, input().split()))
x = 0
for i in ns:
	for j in range(3):
		if ns[j] == i:
			x += 1
o = 'Yes' if x == 5 else 'No'
print(o)
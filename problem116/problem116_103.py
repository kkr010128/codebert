a = input()
b = input()
n = len(a)
count = 0
for i in range(n):
	if a[i] != b[i]: 
		count = count +1
print(count)
from sys import stdin
w = str(input()).lower()
t = stdin.read().split()
counter = 0
for i in t:
	i = i.lower()
	if i == w:
		counter += 1
print(counter)

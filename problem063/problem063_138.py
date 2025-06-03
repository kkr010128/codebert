import fileinput

dict = {}
for i in range(ord("a"), ord("z") + 1):
	dict[chr(i)] = 0

for line in fileinput.input():
	for char in list(line):
		c = char.lower()
		if c in dict:
			dict[c] += 1

# ?????????????????¨?????????.
for i in range(ord("a"), ord("z") + 1):
	print(chr(i), ":", dict[chr(i)])
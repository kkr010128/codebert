import sys
 
string = str()
 
for line in sys.stdin:
    string += line.lower()

alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for letter in alph:
	sum = 0
	n = -1
	while True:
		n = string.find(letter, n + 1)
		if n == -1:
			break
		sum += 1
	print("{} : {}".format(letter, sum))
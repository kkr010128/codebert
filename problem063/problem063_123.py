import sys
counts = [0] * 26

s = sys.stdin.read()
	
for c in s:
	o = ord(c)
	if o >= 65 and o <= 90:
		counts[o - 65] += 1
	elif o >= 97 and o <= 122:
		counts[o - 97] += 1
	
for i in range(len(counts)):
	print(chr(i + 97) + ' : ' + str(counts[i]))


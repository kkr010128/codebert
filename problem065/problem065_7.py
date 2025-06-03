import sys
w = raw_input()
n = 0
for t in sys.stdin.read().split():
	if t == 'END_OF_TEXT':
		break
	if t.lower() == w.lower():
		n += 1
print n
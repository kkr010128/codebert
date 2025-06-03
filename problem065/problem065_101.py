w = input()
t = []
while True:
	temp = input()
	if temp == 'END_OF_TEXT':
		break
	else:
		t += [s.strip(',.') for s in temp.lower().split(' ')]

print(t.count(w))
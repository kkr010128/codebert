
string = [str(i) for i in input()]
for _ in range(int(input())):
	n = input().split()
	order = n.pop(0)
	if order == 'replace':
		string = string[:int(n[0])] + \
		[i for i in n[2]] + string[int(n[1])+1:]
	elif order == 'reverse':
		string = string[:int(n[0])] + \
		string[int(n[0]):int(n[1])+1][::-1] + \
		string[int(n[1])+1:]
	else :
		out = string[ int(n[0]) : int(n[1])+1 ]
		print(''.join(out))
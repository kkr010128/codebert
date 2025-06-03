alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
			'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
			'w','x', 'y', 'z']

dic = {}
for c in alphabet:
	dic[c] = 0

while True:
	try:
		string = list(input().rstrip().lower())
	except EOFError:
		break

	for c in string:
		if c in alphabet:
			dic[c] = dic[c] + 1

for key in dic:
	print('{} : {}'.format(key, dic[key]))

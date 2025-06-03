def dictionary():
	n = int(input())
	s = set()

	for i in range(n):
		command, value = input().split()
		if command == 'insert':
			s.add(value)
		elif command == 'find':
			if value in s:
				print('yes')
			else:
				print('no')

if __name__ == '__main__':
	dictionary()
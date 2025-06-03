a, b = map(int, input().split())
print('a ', end='')
if a < b:
	print('<', end='')
elif a > b:
	print('>', end='')
elif a == b:
	print('==', end='')
print(' b')
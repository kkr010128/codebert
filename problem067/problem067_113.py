n = int(input())
taro,hanako = 0,0
for i in range(n):
	t,h = input().split(' ')
	if t > h:
		taro += 3
	elif t < h:
		hanako += 3
	else:
		taro += 1
		hanako += 1
print('{0} {1}'.format(taro,hanako))
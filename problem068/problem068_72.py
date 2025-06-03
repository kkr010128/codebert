
s = str(input())
q = int(input())

for i in range(q):
	arr = list(map(str, input().split()))
	c = arr[0]
	n1 = int(arr[1])
	n2 = int(arr[2])

	if c == 'print':
		print(s[n1:n2 + 1])
	if c == 'replace':
		s = s[0:n1] + arr[3] + s[n2 + 1:len(s)]
	if c == 'reverse':
		l = n2 - n1 + 1
		reverse = ''
		for i in range(l):
			reverse += s[n2 - i]
		s = s[0:n1] + reverse + s[n2 + 1:len(s)]


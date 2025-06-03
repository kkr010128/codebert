def f1(s,a,b):
	print(s[a:b+1])
	return s

def f2(s,a,b):
	temp = s[a:b+1]
	return s[:a] + temp[::-1] + s[b+1:]

def f3(s,a,b,p):
	return s[:a] + p + s[b+1:]

data = input()
q = int(input())
functions = {'print':f1, 'reverse':f2, 'replace':f3}

for i in range(q):
	temp = [s if s.isalpha() else int(s) for s in input().split(' ')]
	f = temp.pop(0)
	data = functions[f](data,*temp)
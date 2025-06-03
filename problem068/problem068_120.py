st = str(input())
q = int(input())
com = []
for i in range(q):
	com.append(input().split())
for k in com:
	if k[0] == "print":
		print(st[int(k[1]):int(k[2])+1])
	elif k[0] == "reverse":
		s = list(st[int(k[1]):int(k[2])+1])
		s.reverse()
		ss = "".join(s)
		st = st[:int(k[1])] + ss + st[int(k[2])+1:]
	else:
		st = st[:int(k[1])] + k[3] + st[int(k[2])+1:]

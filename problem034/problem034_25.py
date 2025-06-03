face = list(map(int,input().split()))
def Nroll(list):
	a = [list[1],list[5],list[2],list[3],list[0],list[4]]
	return a
def Wroll(list):
	a = [list[2],list[1],list[5],list[0],list[4],list[3]]
	return a
q = int(input())
ql = []
tes = [0,1,2,3,4,5]
for i in range(q):
	qk = list(map(int,input().split()))
	for ii in range(2):
		tes = Wroll(tes)
		for k in range(4):
			tes = Nroll(tes)
			for kk in range(4):
				tes = Wroll(tes)
				if tes[0] == face.index(qk[0]) and tes[1] == face.index(qk[1]):
					ql.append(face[tes[2]])
					break
			else:
				continue
			break
		else:
			continue
		break
for ss in ql:
	print(ss)

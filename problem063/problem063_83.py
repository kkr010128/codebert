a = 'abcdefghijklmnopqrstuvwxyz'
b = [0 for i in range(len(a))]
while True:
	try:
		S = raw_input().lower()
	except:
		break
	for j in range(26):
		b[j] += S.count(a[j])
for i in range(len(a)):
	print str(a[i])+" : "+str(b[i])
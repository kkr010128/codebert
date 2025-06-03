moji=""
while True:
	try:
		t = input()
		moji += t.lower()
	except :
		break
moji2 = [chr(i) for i in range(97,97+26)]

for j in moji2:
	print(j+" : "+str(moji.count(j)))


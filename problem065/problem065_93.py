target=raw_input()
ct=0
flag=0
while True:
	line=raw_input().split(" ")
	for i in line:
		if i.lower()==target.lower():
			ct+=1
		elif i=="END_OF_TEXT":
			print ct
			flag=1
	if flag==1:
		break
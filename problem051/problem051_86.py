while(True):
	H,W=list(map(int,input().split()))
	if H==0 and W==0:
		break
	l1=""
	for i in range(W):
		if i%2==0:
			l1+="#"
		else:
			l1+="."
	l1+="\n"
	l2=""
	for i in range(W):
		if i%2==0:
			l2+="."
		else:
			l2+="#"
	l2+="\n"

	l=""
	for i in range(H):
		if i%2==0:
			l+=l1
		else:
			l+=l2

	print(l)
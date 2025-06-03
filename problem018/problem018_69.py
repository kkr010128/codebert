#python2.7

A=raw_input().split()
B=[]
for i in A:
	if i.isdigit():
		B.append(i)
	else:
		if i=="+":
			B[-1]=str(int(B[-1])+int(B[-2]))
			del B[-2]
		elif i=="-":
			B[-1]=str(int(B[-2])-int(B[-1]))
			del B[-2]
		elif i=="*":
			B[-1]=str(int(B[-1])*int(B[-2]))
			del B[-2]
print B[0]
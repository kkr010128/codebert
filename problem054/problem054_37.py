n = input()
r = range(0,52)
for i in range(0,n):
	x = map(str,raw_input().split(" "))
	y = (int(x[1])-1)/13
	if x[0] == "S":
		y = 0
	elif x[0] == "H":
		y = 1
	elif x[0] =="C":
		y = 2
	else:
		y = 3
	z = (int(x[1])-1)
	r.remove(y*13+z)
s = "S"
for j in range(0,len(r)):
	y = r[j]/13
	z = r[j]%13
	if y ==1:
		s = "H"
	elif y ==2:
		s = "C"
	elif y ==3:
		s ="D"
	print s+" "+str(z+1)
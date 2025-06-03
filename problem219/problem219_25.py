d,e=0,0
for x in list("0"+input()):
	d,e=int(x)+min(e,d),9-int(x)+min(e,d+2)
print(min(d,e))
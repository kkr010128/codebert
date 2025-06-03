import fileinput
 
lines = list(fileinput.input())
 
for x in lines:
	print(x[-4:-1])
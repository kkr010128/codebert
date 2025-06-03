str = input() 

if str[len(str)-1] == "s":
	str = str + "es"
else:
	str = str + "s"

print(str)
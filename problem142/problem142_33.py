n = input()
str_n = list(n)

if str_n[-1] == "3":
	print("bon")
elif str_n[-1] == "0" or str_n[-1] == "1" or str_n[-1] == "6" or str_n[-1] == "8":
	print("pon")
else:
	print("hon")
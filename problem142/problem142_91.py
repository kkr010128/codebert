n = input()
x = list(n)
length = len(x)
if x[length-1] == "3":
    print("bon")
elif x[length-1] == "0" or x[length-1] == "1" or x[length-1] == "6" or x[length-1] =="8":
    print("pon")
else:
    print("hon")
a = [2, 4, 5, 7, 9]
b = [0, 1, 6, 8]
n = input()
if int(n[-1]) in a:
    print("hon")
elif int(n[-1]) in b:
    print("pon")
else:
    print("bon")
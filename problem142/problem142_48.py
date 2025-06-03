n = input()
k = int(n[-1])
if k == 3:
    print("bon")
elif k == 0 or k == 1 or k == 6 or k == 8:
    print("pon")
else:
    print("hon")

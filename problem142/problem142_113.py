N = int(input())

a = N % 10
if a == 0 or a == 1 or a == 6 or a == 8:
    print("pon")
elif a == 3:
    print("bon")
else:
    print("hon")
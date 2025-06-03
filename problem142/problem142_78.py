count = int(input())

if count % 10 == 3:
    print("bon")
elif count % 10 in [0, 1, 6, 8]:
    print("pon")
else:
    print("hon")
N = int(input())

D = N % 10

if D in [2, 4, 5, 7, 9]:
    print("hon")
if D in [0, 1, 6, 8]:
    print("pon")
if D == 3:
    print("bon")
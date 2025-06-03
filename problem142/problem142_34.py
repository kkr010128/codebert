N = int(input())

ans = N % 10

if ans == 2 or ans == 4 or ans == 5 or ans == 7or ans == 9:
    print("hon")
elif ans == 0 or ans == 1 or ans == 6 or ans == 8:
    print("pon")
else:
    print("bon")
INPUT = input().split()
D = int(INPUT[0])
T = int(INPUT[1])
S = int(INPUT[2])

if D/S <= T:
    print("Yes")
else:
    print("No")
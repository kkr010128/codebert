num = input()
L = num.split()
D = int(L[0])
T = int(L[1])
S = int(L[2])
if D / S <= T:
    print("Yes")
else:
    print("No")
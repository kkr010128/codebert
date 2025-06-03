N = input()
tmp = 0
for s in N:
    tmp += int(s)
if tmp%9 == 0:
    print("Yes")
else:
    print("No")
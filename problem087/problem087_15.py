n = input()

ret = 0

for s in n:
    ret *= 10
    ret %= 9
    ret += int(s)
    ret %= 9

if ret == 0:
    print("Yes")
else:
    print("No")
n = str(input())
tmp  = 0
for i in n:
    tmp += int(i)
if tmp % 9 == 0:
    print("Yes")
else:
    print("No")
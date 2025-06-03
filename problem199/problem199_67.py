s = input()
flg = True
while len(s) > 0:
    if s.startswith("hi"):
        s = s[2::]
    else:
        flg = False
        break
if flg:
    print("Yes")
else:
    print("No")
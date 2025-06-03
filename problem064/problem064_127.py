s = input()
p = input()

if len(p) <= len(s) and (s+s).find(p) > -1:
    print("Yes")
else:
    print("No")

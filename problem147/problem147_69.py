s = input()
t = input()

if (s == t[:-1]) & (len(s) + 1 == len(t)):
    print("Yes")
else:
    print("No")

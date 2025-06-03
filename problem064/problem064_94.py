s = input()
p = input()
s += s
if p in s and 2 * len(p) <= len(s):
    print("Yes")
else:
    print("No")
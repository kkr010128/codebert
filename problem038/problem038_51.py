a,b = input().split()
a = int(a)
b = int(b)
sign = "=="
if (a < b) : sign = "<"
if (a > b) : sign = ">"
print("a",sign,"b")
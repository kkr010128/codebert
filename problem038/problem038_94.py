s = input()
s = s.split()
n = []

for i in s:
    n.append(int(i))

a = n[0]
b = n[1]

print("a",end = " ")

if a > b:
    print(">",end = " ")
elif a < b:
    print("<",end = " ")
else:
    print("==",end = " ")

print("b")

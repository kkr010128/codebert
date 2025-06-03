b = []
while True:
    a = input().split()
    if a[1] == "?":
        break
    elif a[1] == "+":
        b.append(int(a[0])+int(a[2]))
    elif a[1] == "-":
        b.append(int(a[0])-int(a[2]))
    elif a[1] == "*":
        b.append(int(a[0])*int(a[2]))
    else:
        b.append(int(a[0])//int(a[2]))

for i in b:
    print(i)

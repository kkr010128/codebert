dic = {}
line = []
for i in range(int(input())):
    line.append(input().split())
for i in line:
    if i[0][0] == "i":
        dic[i[1]] = None
    else:
        print("yes" if i[1] in dic else "no")
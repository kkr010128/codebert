dic = {}
for s in range(int(input())):
    i = input().split()
    if i[0] == "insert":
        dic[i[1]] = None
    else:
        print("yes" if i[1] in dic else "no")
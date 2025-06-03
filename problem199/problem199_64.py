s = input()

hitachi = ""
flag = False

for i in range(5):
    hitachi += "hi"
    if hitachi == s:
        print("Yes")
        flag = True
        break

if flag == False:
    print("No")

# cording: utf-8

num = []

while True:
    list = input().rstrip().split(" ")
    if str(list[1]) == "?":
        break
    num.append(list)

for i in range(len(num)):
    if str(num[i][1]) == "+":
        print(int(num[i][0]) + int(num[i][2]))
    elif str(num[i][1]) == "-":
        print(int(num[i][0]) - int(num[i][2]))
    elif str(num[i][1]) == "*":
        print(int(num[i][0]) * int(num[i][2]))
    else:
        print(int(num[i][0]) // int(num[i][2]))
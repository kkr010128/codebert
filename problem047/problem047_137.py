count = -1
a = []
while True:
    count += 1
    n = input()
    a.append(n.split())
    boy = a[count][0]
    fuck = a[count][1]
    girl = a[count][2]
    if fuck == "+":
        print(int(boy)+int(girl))
    elif fuck == "-":
        print(int(boy)-int(girl))
    elif fuck == "*":
        print(int(boy)*int(girl))
    elif fuck == "/":
        print(int(int(boy)/int(girl)))
    if a[count][1] == "?":
        break
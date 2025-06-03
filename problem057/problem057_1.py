num = []
while True:
    l = map(int, raw_input().split())
    if l[0] == l[1] == l[2] == -1:
        break
    if l[0]*l[1] < 0:
        num.append("F")
    else:
        sum = l[0] + l[1]
        if sum >= 80:
            num.append("A")
        elif sum >= 65:
            num.append("B")
        elif sum >= 50:
            num.append("C")
        elif sum >= 30:
            if l[2] >= 50:
                num.append("C")
            else:
                num.append("D")
        else:
            num.append("F")

for i in range(len(num)):
    print num[i]
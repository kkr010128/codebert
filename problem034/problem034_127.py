d = input().split()
n = int(input())
r_list = []
i = 0

while n > i:
    t, f = map(str, input().split())
    tf = str(d.index(t)) + str(d.index(f))

    if tf == "12" or tf == "24" or tf == "43" or tf == "31":
        r_list.append(1)
    elif tf == "20" or tf == "03" or tf == "35" or tf == "52":
        r_list.append(2)
    elif tf == "01" or tf == "15" or tf == "54" or tf == "40":
        r_list.append(3)
    elif tf == "10" or tf == "51" or tf == "45" or tf == "04":
        r_list.append(4)
    elif tf == "02" or tf == "30" or tf == "53" or tf == "25":
        r_list.append(5)
    elif tf == "21" or tf == "42" or tf == "34" or tf == "13":
        r_list.append(6)

    i += 1

for r in r_list:
    print(d[r-1])


value = int(input())
kyu_rated = 8
lvalue = 400
rvalue = 599
for i in range(0, 8):
    if lvalue <= value <= rvalue:
        print(kyu_rated)
        flag = 1
        break
    else:
        lvalue += 200
        rvalue += 200
        kyu_rated -= 1

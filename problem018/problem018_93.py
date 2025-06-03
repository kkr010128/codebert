Sum = input().split()
cou = 1
while len(Sum) != 1 :
    cou += 1
    if Sum[cou] == '+' :
        del Sum[cou]
        Sum.insert((cou - 2) ,int(Sum.pop(cou - 2)) + int(Sum.pop(cou - 2)))
        cou -= 2
    elif Sum[cou] == '-' :
        del Sum[cou]
        Sum.insert((cou - 2) ,int(Sum.pop(cou - 2)) - int(Sum.pop(cou - 2)))
        cou -= 2
    elif Sum[cou] == '*' :
        del Sum[cou]
        Sum.insert((cou - 2) ,int(Sum.pop(cou - 2)) * int(Sum.pop(cou - 2)))
        cou -= 2

print(Sum[0])
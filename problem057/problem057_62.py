while True :
    a, b, c = [int(temp) for temp in input().split()]
    if a == b == c == -1 : break
    if   (a == -1) or (b == -1) or (a + b < 30) : print('F')
    elif (80 <= a + b) : print('A')
    elif (65 <= a + b) : print('B')
    elif (50 <= a + b) or ((30 <= a + b) and (50 <= c)) : print('C')
    else : print('D')
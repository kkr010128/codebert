X, Y= input().split()
IX = int(X)
IY = int(Y)
C = 2
T = 4
i = 0

while i <= IX:
    

    
    if ((C*i) + (T*(IX-i))) == IY:
        print('Yes')
        break
    elif i == IX:
        print('No')
        break
    else:
        i = i + 1
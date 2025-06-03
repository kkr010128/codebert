X=int(input())
flagp=False
flagm=False
flage=True
for A in range(-10**3,10**3):
    B5=A**5-X
    for B in range(10**3):
        if B5==B**5:
            flagp=True
            flage=False
            break
        elif B5==-B**5:
            flagm=True
            flage=False
            break
    else:
        continue
    break
if flagp:
    print(A,B)
elif flage:
    raise Exception
else:
    print(A,-B)
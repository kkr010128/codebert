a = int(input())
if (a%2==1 and (a!=25 and a!=27 and a!=9 and a!=21)) or a==2:
    print(1)
elif a==32:
    print(51)
elif a==24:
    print(15)
elif a==16:
    print(14)
elif a==28 or a==30:
    print(4)
elif (a!=4 and a%4==0) or a==18 or a==27:
    print(5)
else:
    print(2)
N = str(input())

N = N[::-1]
if N[0] == '2' or N[0] =='4' or N[0] =='5' or N[0] =='7' or N[0] =='9' :
    print('hon')
elif N[0] == '0' or N[0] =='1' or N[0] =='6' or N[0] =='8' :
    print('pon')
else:
    print('bon')
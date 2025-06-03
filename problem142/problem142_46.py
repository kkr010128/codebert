digitsStr = input()
honlist = ["2","4","5","7","9"]
ponList = ["0","1","6","8"]
if digitsStr[-1] == '3':
    print('bon')
elif digitsStr[-1] in honlist:
    print('hon')
elif digitsStr[-1] in ponList:
    print('pon')
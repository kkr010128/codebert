N = input()
if N.endswith('2') == True or N.endswith('4') == True or N.endswith('5') == True or N.endswith('7') == True or N.endswith('9') == True:
    print('hon')
elif N.endswith('0') == True or N.endswith('1') == True or N.endswith('6') == True or N.endswith('8') == True:
    print('pon')
else:
    print('bon')
N = input()
if (N[-1] == str(3)):
    print('bon')
elif(int(N[-1]) == 0 or int(N[-1]) == 1 or int(N[-1]) == 6 or int(N[-1]) == 8 ):
    print('pon')
else:
    print('hon')
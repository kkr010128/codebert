N = input()

lastWord = int(N[-1])
if lastWord == 3:
    print('bon')
elif lastWord == 0 or lastWord == 1 or lastWord == 6 or lastWord == 8:
    print('pon')
else:
    print('hon')





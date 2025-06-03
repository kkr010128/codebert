N = int(input())
if N-(N//10*10)==3:
    print('bon')
elif N-(N//10*10)==0 or N-(N//10*10)==1 or N-(N//10*10)==6 or N-(N//10*10)==8:
    print('pon')
else:
    print('hon')
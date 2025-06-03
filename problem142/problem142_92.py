N = int(input())
number1 = [2,4,5,7,9]
number2 = [3]
number3 = [0,1,6,8]
if N % 10 in number1:
    print('hon')
elif N % 10 in number2:
    print('bon')
elif N % 10 in number3:
    print('pon')
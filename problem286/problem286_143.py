num = input()

num1,num2 = num.split(' ')

num1 = int(num1)
num2 = int(num2)

if num1 > 9 or num2 > 9:
    print('-1')
else:
    print (num1 * num2)
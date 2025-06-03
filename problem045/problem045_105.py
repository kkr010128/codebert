a, b = [int(i) for i in input().split(" ")]
num1 = a // b
num2 = a % b
num3 = "{:.8f}".format(a / b)

print(num1, num2, num3)
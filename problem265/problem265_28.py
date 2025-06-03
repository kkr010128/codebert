import math
num1 = int(input())
num2 = math.floor(num1 / 1.08)
num3 = math.ceil(num1 / 1.08)
end = False
if math.floor(math.floor(num1 / 1.08) * 1.08) == num1:
  print(math.floor(num1 / 1.08))
  end = True
elif math.floor(math.ceil(num1 / 1.08) * 1.08) == num1 and end == False:
  print(math.ceil(num1 / 1.08))
else:
  print(':(')
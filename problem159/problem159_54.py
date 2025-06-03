import math
x = int(input())
initial = 100
count = 0
while initial < x:
  initial += initial//100  
  count += 1
print(count)
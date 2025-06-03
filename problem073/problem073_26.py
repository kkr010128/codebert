import math

case_num = 0

N = int(input())

for num in range(N - 1):
  num += 1
  
  case_num += ( math.ceil(N / num) - 1 )


print(case_num)
# coding: utf-8
# Your code here!

n = int(input())

sum = 100000
for i in range(n):
   sum += sum * 0.05
   if sum % 1000 > 0:
      sum -= sum % 1000
      sum += 1000

print(int(sum))

n = input()
n = int(n)
seq = input().split()
sumNum = 0
minNum = 1000000
maxNum = -1000000
for numT in seq:
 num = int(numT)
 if(num > maxNum):
  maxNum = num
 if(num < minNum):
  minNum = num
 sumNum+=num
print(minNum,maxNum,sumNum)

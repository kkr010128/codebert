__author__= 'CIPHER'

str = input()
numList = str.split(' ')
numList = [ int(x) for x in numList]
#print(numList)
result = 1
length = 0
for x in numList:
    result *= x
    length += x

print(result,2*length)
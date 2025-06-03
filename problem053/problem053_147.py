i=0
j = int(input())
numlist = list(int(i) for i in input().split())

while i < j-1:
  print(numlist[j-i-1],end='')
  print(' ',end='')
  i += 1
print(numlist[0])
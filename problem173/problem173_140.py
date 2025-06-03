n = int(input())
num = [int(x) for x in range(1,n+1)]

for i in num:
  if (i%3 == 0) or (i%5 == 0):
    num[i-1] = 0
    
print(sum(num))
score = int(input())
levelList = [600,800,1000,1200,1400,1600,1800]
level = 8

for i in range(7):
 if score < levelList[i]:
  break
 else :
  level = level - 1
print(level)
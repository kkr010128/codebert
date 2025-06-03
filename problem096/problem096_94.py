firstLine = input()
numOfPoints, limitDisatnce = list(map(int,firstLine.split(' ')))[0], list(map(int,firstLine.split(' ')))[1]
points = []
for i in range(0, numOfPoints):
  cordinate = list(map(int,input().split(' ')))
  points.append(cordinate)

count = 0
for i in range(0, len(points)):
  distance = (points[i][0] ** 2) + (points[i][1] ** 2)
  if (limitDisatnce ** 2) >= distance:
    count = count + 1

print(count)
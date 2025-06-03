import math

numbers = input().split(" ")
numbers = [int(x) for x in numbers]
N = numbers[0]
D = numbers[1]

return_value =0

for i in range(N):
    coordinates = input().split(" ")
    coordinates = [int(x) for x in coordinates]
    x_coor = coordinates[0]
    y_coor = coordinates[1]
    distance = math.sqrt((x_coor ** 2) + (y_coor ** 2))
    if distance <= D:
        return_value += 1

print(return_value)
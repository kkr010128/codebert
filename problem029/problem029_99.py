import math
val = str(input()).split()

numList = list(map(float, list(val)))

print(math.sqrt(((numList[2]-numList[0]) ** 2) + ((numList[3]-numList[1]) ** 2)))

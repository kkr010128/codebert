import math

input = int(input())

hour = math.floor(input/3600)
input -= hour*3600

min = math.floor(input/60)
input -= min*60

sec = math.floor(input)

print(str(hour)+":"+str(min)+":"+str(sec))


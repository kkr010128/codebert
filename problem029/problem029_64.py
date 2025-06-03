import math
#1st line
pos_x1, pos_y1, pos_x2, pos_y2 = map(float,input().split(" "))

dist = math.sqrt((pos_x1-pos_x2)**2 + (pos_y1 - pos_y2)**2)
print(str(dist))
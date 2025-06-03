# -*- coding: utf-8 -*-

x = []
y = []

while ( 1 ):
    
    temp_x, temp_y = map(int, input().split() )
    
    if (temp_x == 0 and temp_y == 0):
        break

    if (temp_y < temp_x):
        temp_x, temp_y = temp_y, temp_x

    x.append(temp_x)
    y.append(temp_y)

for (i,j) in zip(x,y):
    print(i,j)
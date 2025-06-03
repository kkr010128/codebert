# -*- coding: utf-8 -*-

x = []
while ( 1 ):
    
    temp = int( input() )
    
    if (temp == 0):
        break

    x.append(temp)

index = 1
for i in x:
    print('Case {0}: {1}'.format(index, i))
    index += 1
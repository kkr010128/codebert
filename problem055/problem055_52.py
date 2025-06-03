# coding:utf-8
import sys
n = input()
array = []
for i in range(n):
    array.append(map(int, raw_input().split()))
array.sort()
result = [[0 for i in range(4)] for j in range(n)]
index = 0
result[index] = array[0][0:4]
for i in range(1,n):
    if result[index][0:3] == array[i][0:3]:
        result[index][3] += array[i][3]
    elif result[index][0:3] != array[i][0:3]:
        index += 1
        result[index] = array[i][0:]
index = 0
for i in range(4):
    for j in range(3):
        for k in range(10):
            sys.stdout.write(' ')
            if(i == result[index][0] - 1 and j == result[index][1] - 1 and k == result[index][2] - 1):
                print result[index][3],
                if index != len(result) - 1:
                    index += 1
            else:
                print 0,
        else:
            print
    else:
        if(i != 3):
            print "####################"


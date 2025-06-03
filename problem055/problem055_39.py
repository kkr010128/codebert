# -*-coding:utf-8

import fileinput
import math

def main():
    offiHouse = [[[0 for i3 in range(10)] for i2 in range(3)] for i1 in range(4)]   #y, x, z

    n = int(input())

    for i in range(n):
        a, b, c, d = map(int, input().split())

        offiHouse[a-1][b-1][c-1] += d

    for i in range(4):
        for j in range(3):
            for k in range(10):
                print('', offiHouse[i][j][k], end='')
            print()
        if(i != 3):
            print('#' * 20)

if __name__ == '__main__':
    main()
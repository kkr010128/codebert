# -*-coding:utf-8

import fileinput
import math

def main():

    for line in fileinput.input():
        a, b, c = map(int, line.strip().split())

        if(a < b and b <c):
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    main()
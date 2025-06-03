# -*-coding:utf-8

import fileinput
import math

def main():
    for line in fileinput.input():
        a, b, c = map(int, line.strip().split())

        count = 0
        for i in range(a, b+1):
            if(c % i == 0):
                count += 1

        print(count)

if __name__ == '__main__':
    main()
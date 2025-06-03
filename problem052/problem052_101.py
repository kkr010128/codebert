# -*-coding:utf-8

#import fileinput
import math

def main():

    n = int(input())

    for i in range(1, n+1):
        x = i
        if (x%3 == 0):
            print(' %d' % i, end='')
        else:
            while(x):
                if (x%10 == 3):
                    print(' %d' % i, end='')
                    break
                else:
                    x = int(x/10)

    print('')

if __name__ == '__main__':
    main()
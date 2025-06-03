# -*- coding: utf-8 -*-
import math
def main():
    N = int(input())
    if N % 1.08 == 0:
        print(N/1.08)
    else:
        x = math.ceil(N/1.08)
        if x < (N+1)/1.08:
            print(x)
        else:
            print(':(')
    return
if __name__ == '__main__':
    main()
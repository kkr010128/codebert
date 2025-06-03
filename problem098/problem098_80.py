import sys
import math
sys.setrecursionlimit(500000)
INF = float('inf')

def main():
    n = int(input())
    c = input()
    red_stones = c.count('R')
    return c[red_stones:].count('R')

if __name__ == '__main__':
    print(main())

import sys
sys.setrecursionlimit(4100000)
import math
INF = 10**9

def main():
    S = input()

    weeks = ['SUN','MON','TUE','WED','THU','FRI','SAT']
    for i in range(len(weeks)):
        if weeks[i] == S:
            print(7-i)
            return


if __name__ == '__main__':
    main()

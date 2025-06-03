# -*- coding: utf-8 -*-
import sys

def main():
    N = int( sys.stdin.readline() )
    A_list = list(map(int, sys.stdin.readline().split()))

    A_list.sort(reverse=True)
    arrived_idx = 1
    comfort = A_list[0]


    for i in range(1, len(A_list)):
        if ( len(A_list) - 1 - arrived_idx ) >= 2:
            comfort += (A_list[i] * 2)
            arrived_idx += 2
        elif ( len(A_list) - 1 - arrived_idx ) == 1:
            comfort += A_list[i]
            break
        else:  # ( len(A_list) - 1 - arrived_idx ) == 0:
            break


    print(comfort)


if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
import sys


def main():
    N,K = list(map(int, sys.stdin.readline().split()))
    A_list = list(map(int, sys.stdin.readline().split()))
    

    for i in range(K, len(A_list)):
        if A_list[i] > A_list[i-K]:
            print("Yes")
        else:
            print("No")



if __name__ == "__main__":
    main()

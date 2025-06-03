#!/usr/bin/env python3
from typing import *

YES = 'Yes'
NO = 'No'

# def solve(D: int, T: int, S: int) -> str:
def solve(D, T, S):
    return YES if D <= T*S else NO
    

def main():
    D, T, S = map(int, input().split())
    a = solve(D, T, S)
    print(a)

if __name__ == '__main__':
    main()

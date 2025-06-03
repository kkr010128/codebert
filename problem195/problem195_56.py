
import numpy as np
from functools import *
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline



def acinput():
    return list(map(int, input().split(" ")))


def II():
    return int(input())

directions=np.array([[1,0],[0,1],[-1,0],[0,-1]])
directions = list(map(np.array, directions))

mod = 10**9+7


def factorial(n):
    fact = 1
    for integer in range(1, n + 1):
        fact *= integer
    return fact



def serch(x, count):
    #print("top", x, count)
            

    for d in directions:
        nx = d+x
        #print(nx)
        if np.all(0 <= nx) and np.all(nx < (H, W)):
            if field[nx[0]][nx[1]] == "E":
                count += 1 
                field[nx[0]][nx[1]] = "V"
                count = serch(nx, count)  
                continue
            if field[nx[0]][nx[1]] == "#":
                field[nx[0]][nx[1]] = "V"
                count = serch(nx, count)    
                 
    return count

K=int(input())
s = [1, 1, 1, 2, 1, 2, 1, 5, 2, 2, 1, 5, 1, 2, 1, 14,
     1, 5, 1, 5, 2, 2, 1, 15, 2, 2, 5, 4, 1, 4, 1, 51]

print(s[K-1])


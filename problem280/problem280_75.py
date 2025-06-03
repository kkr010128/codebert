import sys
import math
import itertools
from collections import defaultdict, deque
from copy import deepcopy

    
input = sys.stdin.readline
def RD(): return input().rstrip()
def F(): return float(input().rstrip())
def I(): return int(input().rstrip())
def MI(): return map(int, input().split())
def MF(): return map(float,input().split())
def LI(): return tuple(map(int, input().split()))
def LF(): return list(map(float,input().split()))
def Init(H, W, num): return [[num for i in range(W)] for j in range(H)]
    
    
def main():
    N = I()
    mylist = [LI() for i in range(N)]
    dist = [[0 for i in range(N)] for i in range(N)]
    for index1, num1 in enumerate(mylist):
        for index2, num2 in enumerate(mylist):
            dist[index1][index2] = math.sqrt((num1[0]-num2[0])**2 + (num1[1]-num2[1])**2)
    result = 0
    index = 0
    seq = [i for i in range(N)]
    for i in itertools.permutations(seq):
        index += 1
        past = i[0]
        for num in i[1:]:
            result += dist[past][num]
            past = num
            
            
    print(result/index)

    
    
    
if __name__ == "__main__":
    main()
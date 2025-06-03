    
from enum import Enum
import sys

BIG_NUM = 2000000000
MOD = 1000000007
EPS = 0.000000001


class Type(Enum):
    win_Taro = 0
    win_Hanako = 1
    EVEN = 2

def comp_str(A,B):
    if A > B:
        return Type.win_Taro
    elif A < B:
        return Type.win_Hanako
    else:
        return Type.EVEN

N = int(input())

point_Taro = 0
point_Hanako = 0

for loop in range(N):
    line = str(input()).split()
    ret_type = comp_str(line[0],line[1])
    if ret_type == Type.win_Taro:
        point_Taro += 3
    elif ret_type == Type.win_Hanako:
        point_Hanako += 3
    else:
        point_Taro += 1
        point_Hanako += 1

print("%d %d"%(point_Taro,point_Hanako))

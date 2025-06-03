from enum import Enum

class Type(Enum):
    win_Taro = 0
    win_Hanako = 1
    Even = 2

def comp_str(A, B):
    if A > B:
        return Type.win_Taro
    elif A < B:
        return Type.win_Hanako
    else:
        return Type.Even

N = int(input())

point_Taro = 0
point_Hanako = 0

for loop in range(N):
    line = str(input()).split()
    ret_type = comp_str(line[0], line[1])
    if ret_type == Type.win_Taro:
        point_Taro += 3
    elif ret_type == Type.win_Hanako:
        point_Hanako += 3
    else:
        point_Taro += 1
        point_Hanako += 1

print("%d %d"%(point_Taro, point_Hanako))

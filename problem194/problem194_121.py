import math
from functools import lru_cache

@lru_cache(maxsize = None)
def count_change_point_min(r , c , current_color):
    min_values = list()
    if r != h-1:
        min_values.append(count_change_point_min(r+1, c, S[r][c]))
    if c != w-1:
        min_values.append(count_change_point_min(r, c+1, S[r][c]))
    if len(min_values) == 0:
        min_values.append(0)
        
    return min(min_values) + (0 if S[r][c] == current_color else 1)
    
    
h,w = map(int,input().split())
S = list()
for _ in range(h):
    S.append(list(input()))
    
if S[0][0] == ".":
    ceil_or_floor = math.floor
else:
    ceil_or_floor = math.ceil
    
print (ceil_or_floor((count_change_point_min(0, 0, S[0][0])+1) / 2))
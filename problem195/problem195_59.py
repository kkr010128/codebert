import sys
def input(): return sys.stdin.readline().rstrip()
series = [1, 1, 1, 2, 1, 2, 1, 5, 
          2, 2, 1, 5, 1, 2, 1, 14, 
          1, 5, 1, 5, 2, 2, 1, 15, 
          2, 2, 5, 4, 1, 4, 1, 51]

print(series[int(input())-1])
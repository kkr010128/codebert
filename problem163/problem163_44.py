import sys
input = sys.stdin.readline

"""

"""

s, w = map(int, input().split())
if w >= s:
    print("unsafe")
else:
    print("safe")
import math
from collections import deque
def main():
    t = [int(t)for t in input().split()]
    x,y = t[0],t[1]

    earned = 0

    if x == 1:
        earned += 300000
    elif x == 2:
        earned += 200000
    elif x == 3:
        earned += 100000
    if y == 1:
        earned += 300000
    elif y == 2:
        earned += 200000
    elif y == 3:
        earned += 100000

    if x == y and x == 1:
        earned += 400000

    print(earned)
if __name__ == "__main__":
    main()
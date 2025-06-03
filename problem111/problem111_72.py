import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
from collections import deque
def main():
    n, *a = map(int, read().split())
    a.sort(reverse=True)
    a = deque(a)
    circle_joined = deque()
    next_score = a.popleft()
    r = 0
    flag = False
    while a:
        circle_joined.append(a.popleft())
        if flag:
            next_score = circle_joined.popleft()
            r += next_score
            flag = False
        else:
            r += next_score
            flag = True
    print(r)

if __name__ == '__main__':
    main()

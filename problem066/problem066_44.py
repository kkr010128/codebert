from collections import deque
while True:
    s = input()
    if s == '-': break
    else: ds = deque(s)
    ds.rotate(sum([int(input()) for _ in range(int(input()))])*-1)
    print(''.join(ds))
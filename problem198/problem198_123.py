import sys
from collections import deque
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7

def main():
    N = int(readline())
    if N==1:
        print('a')
        exit()
    d = deque(['a'])
    ans = []
    while d:
        s = d.popleft()
        last = ord(max(s))
        for i in range(97,last+2):
            S = s + chr(i)
            if len(S)==N:
                ans.append(S)
            else:
                d.append(S)
    ans.sort()
    for s in ans:
        print(s)
if __name__ == '__main__':
    main()
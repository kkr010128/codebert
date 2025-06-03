import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
from collections import defaultdict 
def main():
    N = int(input())
    ans = defaultdict(int)
    for i in range(1, 110):
        for j in range(1, 110):
            for k in range(1, 110):
                v = i*i+j*j+k*k+i*j+j*k+k*i
                ans[v] += 1
    for i in range(1, N+1):
        print(ans[i])
if __name__ == '__main__':
    main()

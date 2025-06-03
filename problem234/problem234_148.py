import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

from collections import defaultdict

def f(x):
    return (int(str(x)[0]), int(str(x)[-1])) 
def main():
    N = int(readline())
    df = defaultdict(int)
    for i in range(1, N+1):
        df[f(i)] += 1
    ans = 0
    for i in range(1, 10):
        for j in range(1, 10):
            ans +=  df[(i, j)]*df[(j, i)]
    print(ans)
if __name__ == '__main__':
    main()

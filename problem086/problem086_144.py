import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
 
def main():
    N, X, T = map(int, readline().split())
    p = (N//X)*T
    if N%X == 0:
        print(p)
    else:
        print(p+T)
if __name__ == '__main__':
    main()

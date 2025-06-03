import sys
readline = sys.stdin.readline

def main():
    A, V = map(int, readline().rstrip().split())
    B, W = map(int, readline().rstrip().split())
    T = int(readline())

    v = V - W
    if v <= 0:
        print('NO')
        return
    
    if abs(A - B) / v > T:
        print('NO')
    else:
        print('YES')

if __name__ == '__main__':
    main()
import sys
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7

def main():
    M1, D1 = map(int, readline().split())
    M2, D2 = map(int, readline().split())
    if M1 != M2:
        print('1')
    else:
        print('0')

if __name__ == '__main__':
    main()
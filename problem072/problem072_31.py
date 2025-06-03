import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

def main():
    N = int(readline())
    cnt = 0
    ans = -1
    for _ in range(N):
        x, y = map(int, readline().split())    
        if x == y:
            cnt += 1
            ans = max(ans, cnt)
        else:
            cnt = 0
    if ans >=3:
        print('Yes') 
    else:
        print('No')
if __name__ == '__main__':
    main()

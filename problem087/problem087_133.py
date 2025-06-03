import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
 
def main():
    N = input()
    s = 0
    for i in range(len(N)):
        s += int(N[i])
    if s%9 == 0:
        print('Yes')
    else:
        print('No')
if __name__ == '__main__':
    main()

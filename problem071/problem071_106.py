import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
 
def main():
    S = input()
    if S[-1] == 's':
        print(S+'es')
    else:
        print(S+'s')
if __name__ == '__main__':
    main()

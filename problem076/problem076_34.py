import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
 
def main():
    x = int(readline())
    if x:
        print(0)
    else:
        print(1)

if __name__ == '__main__':
    main()

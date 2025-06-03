import sys

input = sys.stdin.readline

def main():
    s = input().rstrip('\n')
    if s[-1] == 's':
        s += 'es'
    else:
        s += 's'

    print(s)

if __name__ == '__main__':
    main()
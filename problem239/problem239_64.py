import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    c = input()
    str = list('abcdefghijklmnopqrstuvwxyz')
    print(str[str.index(c)+1])

if __name__ == '__main__':
    main()
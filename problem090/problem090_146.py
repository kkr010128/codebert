import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
def main():
    s = input()
    if 'RRR' in s:
        print(3)
    elif 'RR' in s:
        print(2)
    elif 'R' in s:
        print(1)
    else:
        print(0)

if __name__ == '__main__':
    main()
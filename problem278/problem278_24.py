from sys import stdin

def main():
    r = int(stdin.readline())

    if r < 1:
        print(0)
    else:
        circle = r * r
        print(circle)

if __name__ == '__main__':
    main()
import sys
input = sys.stdin.readline
def main():
    X = int(input())
    NUM = X//100
    A = X%100
    if A <= NUM*5:
        print(1)
    else:
        print(0)

if __name__ == '__main__':
    main()
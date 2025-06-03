import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    mark = 1
    remain = 0
    for i in range(n):
        if a[i] == mark:
            remain += 1
            mark += 1
    if remain == 0:
        print(-1)
    else:
        print(n-remain)

if __name__ == '__main__':
    main()
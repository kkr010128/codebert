#!/usr/bin/env python3
def main():
    N = int(input())
    print('YES' if len(set(input().split())) == N else 'NO')


if __name__ == '__main__':
    main()

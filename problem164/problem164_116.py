#!/usr/bin/env python3
def main():
    A, B, C, D = map(int, input().split())

    print('Yes' if - (-A // D) >= -(-C // B) else 'No')


if __name__ == '__main__':
    main()

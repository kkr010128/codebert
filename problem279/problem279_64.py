def main():
    import sys
    readline = sys.stdin.buffer.readline

    n = int(readline())
    s = readline().rstrip().decode('utf-8')

    print('Yes' if s[:n//2] == s[n//2:] else 'No')

if __name__ == '__main__':
    main()
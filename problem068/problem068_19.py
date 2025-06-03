#!usr/bin/env python3

import sys


def main():
    s = sys.stdin.readline().strip('\n')
    q = int(sys.stdin.readline().strip('\n'))

    for instruction in range(q):
        words = [word for word in sys.stdin.readline().strip('\n').split()]
        if words[0] == 'replace':
            s = s[:int(words[1])] + words[3] + s[int(words[2])+1:]
        elif words[0] == 'reverse':
            s = s[:int(words[1])] \
                    + ''.join(reversed(s[int(words[1]):int(words[2])+1])) \
                    + s[int(words[2])+1:]
        elif words[0] == 'print':
            print(s[int(words[1]):int(words[2])+1])


if __name__ == '__main__':
    main()
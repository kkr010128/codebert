import sys


def main():
    _ = int(input())

    imps = sys.stdin.readlines()

    db = {}
    for imp in imps:
        c, k = imp.split(' ')
        if c == 'insert':
            db[k] = 0
        elif k in db:
            print('yes')
        else:
            print('no')


main()
import sys
import string


def main():
    tmp = ''

    try:
        while True:
            tmp += input()
    except EOFError:
        pass

    tmp = list(filter(lambda x: x in string.ascii_lowercase, tmp.lower()))

    for c in string.ascii_lowercase:
        print('{} : {}'.format(c, tmp.count(c)))

    return 0


if __name__ == '__main__':
    sys.exit(main())


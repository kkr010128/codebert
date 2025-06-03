def main(s, w):
    if s > w:
        return 'safe'
    else:
        return 'unsafe'


if __name__ == '__main__':
    S, W = map(int, input().split(' '))
    print(main(S, W))

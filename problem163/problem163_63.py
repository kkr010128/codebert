def main():
    S, W = map(int, input().split())
    cond = S <= W
    print('unsafe' if cond else 'safe')


if __name__ == '__main__':
    main()

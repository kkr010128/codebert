def main():
    sw = list(map(int, input().split()))
    print('unsafe' if sw[0] <= sw[1] else 'safe')

if __name__ == '__main__':
    main()
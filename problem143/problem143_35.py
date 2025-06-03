def Qb():
    k = int(input())
    s = input()

    if len(s) <= k:
        print(s)
    else:
        print(f'{s[:k]}...')


if __name__ == '__main__':
    Qb()

def main():
    cands = {'ABC', 'ARC'}

    S = input()
    cands.discard(S)

    print(cands.pop())


if __name__ == '__main__':
    main()

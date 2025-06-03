def main():
    S = input()
    ans = [s if s != '?' else 'D' for s in S]
    print(''.join(ans))

if __name__ == '__main__':
    main()
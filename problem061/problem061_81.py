def main():
    line = input()

    for ch in line:
        if   65 <= ord(ch) <= 90:
            ch = chr(ord(ch)+32)
        elif 97 <= ord(ch) <= 122:
            ch = chr(ord(ch)-32)

        print(ch, end='')
    print()

if __name__ == '__main__':
    main()


def main():
    s = input()
    if s.count('hi') == len(s) // 2 and len(s) % 2 == 0:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
import sys
def main():
    s = input()
    if len(s) % 2 == 1:
        print('No')
        sys.exit()
    s1 = s[::2]
    s2 = s[1::2]
    s1t = [c == 'h' for c in s1]
    s2t = [c == 'i' for c in s2]
    if all(s1t) and all(s2t):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()

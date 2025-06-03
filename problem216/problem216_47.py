def main():
    a, b, c = map(int, input().split())
    if a == b == c:
        print('No')
    elif a != b and b != c and c != a:
        print('No')
    else:
        print('Yes')
        
if __name__ == '__main__':
    main()
def main():
    h, n = map(int, input().split())
    a = [int(x) for x in input().split()]
    if h > sum(a):
        print('No')
    else:
        print('Yes')
        
if __name__ == '__main__':
    main()
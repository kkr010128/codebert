def main():
    h = int(input())
    w = int(input())
    n = int(input())
    if n % max(h,w) == 0:
        print(n//max(h,w))
    else:
        print(n//max(h,w) + 1)

if __name__=='__main__':
    main()

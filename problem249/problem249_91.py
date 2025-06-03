def main():
    a, b, k = map(int, input().split())
    if k >= a and b >= k-a:
        print(0, b-(k-a))
    elif k >= a and b < k-a:
        print(0, 0)
    else:
        print(a-k, b)
        
if __name__ == '__main__':
    main()


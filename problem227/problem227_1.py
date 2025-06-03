def main():
    n, k = map(int, input().split())
    inlis = list(map(int, input().split()))
    inlis.sort()
    #print(inlis)

    if k >= n:
        print(0)
        exit()
    elif k > 0:
        total = sum(inlis[:-k])
    elif k == 0:
        total = sum(inlis)
    print(total)

    
if __name__ == "__main__":
    main()

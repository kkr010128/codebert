def main():
    n, *xy = map(int, open(0).read().split())
    f = [(i - j, i + j) for i, j in zip(xy[::2], xy[1::2])]
 
    a = max(x[0] for x in f)
    b = min(x[0] for x in f)
 
    c = max(x[1] for x in f)
    d = min(x[1] for x in f)
 
    ans = max(a - b, c - d)
    print(ans)
 
 
if __name__ == '__main__':
    main()
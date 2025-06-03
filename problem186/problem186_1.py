def main():
    k,n = map(int, input().split())
    s = list(map(int, input().split()))
    l = []
    for i in range(n):
        if i == 0:
            l.append(k - (s[-1] - s[0]))
        else:
            a = s[i] - s[i-1]
            l.append(a)
    print(k - max(l))

if __name__ == '__main__':
    main()

def main():
    n = int(input())
    a = [0,0]
    for i in range(1, n+1):
        a[0] += 1
        a[1] = a[1] + 1 if i % 2 != 0 else a[1]
    print(a[1] / a[0])

if __name__ == '__main__':
    main()
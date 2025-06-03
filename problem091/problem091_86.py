def main():
    n = int(input())
    l = list(map(int, input().split()))
    count = 0
    for i in range(n):
        for j in range(i, n):
            for k in range(j, n):
                if l[i] != l[j] and l[j] != l[k] and l[k] != l[i] and l[i]+l[j] > l[k] and l[j]+l[k] > l[i] and l[k]+l[i] > l[j]:
                    count += 1
    print(count)


if __name__ == '__main__':
    main()

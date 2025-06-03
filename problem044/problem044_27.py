if __name__ == '__main__':
    a, b, c = [int(i) for i in input().split()]
    ans = [1 if c % i == 0 else 0 for i in range(a, b + 1)]
    print(sum(ans))
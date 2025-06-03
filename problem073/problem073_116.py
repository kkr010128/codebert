def main():
    n = int(input())
    ab_max = n-1
    ans = sum(ab_max // a for a in range(1, n))
    return ans


if __name__ == '__main__':
    print(main())

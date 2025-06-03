def main():
    N = int(input())
    ans = [0]*(N)
    for x in range(1, 105):
        for y in range(1, 105):
            for z in range(1, 105):
                if N < x**2 + y**2 + z**2 + x*y + y*z + z*x:
                    break
                ans[x**2 + y**2 + z**2 + x*y + y*z + z*x - 1] += 1

    print(*ans, sep="\n")


if __name__ == '__main__':
    main()

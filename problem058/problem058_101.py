def how_many_ways(n, x):
    ways = 0
    for i in range(1, n-1):
        for j in range(i+1, n):
            for k in range(j+1, n+1):
                if i+j+k == x:
                    ways += 1

    return ways

def main():
    while True:
        n, x = [int(x) for x in input().split()]
        if n == x == 0:
            break

        print(how_many_ways(n, x))

if __name__ == '__main__':
    main()


def main():

    n, m = map(int, (input().split()))
    a = [list(map(int, list(input().split()))) for item in range(n)]
    b = [int(input()) for item in range(m)]

    c = [sum(a_im * b_m for (a_im, b_m) in zip(a_i, b)) for a_i in a]
    for c_i in c:
        print(c_i)


main()
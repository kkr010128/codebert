def main():
    N = []
    while True:
        x = input()
        if x == '0':
            break
        else:
            N.append(x)

    for n in N:
        ans = sum(map(int, list(n)))
        print(ans)

main()
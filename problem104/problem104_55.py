def main():
    L, R, d = map(int, input().split(' '))
    total = 0
    for i in range(L, R + 1):
        if i % d == 0:
            total += 1
    print(total)
main()
def main():
    N = int(input())
    for i in range(1, 10):
        if N // i < 10 and N % i == 0:
            print('Yes')
            return
    print('No')

main()
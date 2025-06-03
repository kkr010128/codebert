def main():
    A, B, C = (int(x) for x in input().split())
    K = int(input())

    while not A < B < C and K > 0:
        if A >= B: B *= 2
        else: C *= 2
        K -= 1
        # print(A, B, C, K)
    if A < B < C: print('Yes')
    else: print('No')

if __name__ == '__main__':
    main()
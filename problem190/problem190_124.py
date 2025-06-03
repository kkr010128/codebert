def main():
    S = input()
    N = len(S)
    S1 = S[0:(N - 1) // 2]
    S2 = S[(N + 3) // 2 - 1:]
    
    if S == S[::-1] and S1 == S1[::-1] and S2 == S2[::-1]:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
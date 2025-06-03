def ALDS1_5A():
    n, A, q = int(input()), list(map(int, input().split())), int(input())
    S=[False for i in range(2001)]
    for a in A:
        for i in range(2001-a, 0, -1):
            if S[i]: S[i+a] = True
        S[a] = True
    for mi in input().split():
        if S[int(mi)]:
            print('yes')
        else:
            print('no')

if __name__ == '__main__':
    ALDS1_5A()
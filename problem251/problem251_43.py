def mi():
    return map(int, input().split())

def main():
    N, K = mi()
    R, S, P = mi()
    T = input()
    pt = 0
    my_choices = ['']*N

    for i in range(K):
        tmp = T[i::K]
        for j in range(len(tmp)):
            if j == 0:
                if tmp[j] == 'r':
                    my_choices[i] = 'p'
                    pt += P
                if tmp[j] == 's':
                    my_choices[i] = 'r'
                    pt += R
                if tmp[j] == 'p':
                    my_choices[i] = 's'
                    pt += S
            else:
                if tmp[j] == 'r' and my_choices[i+(j-1)*K] != 'p':
                    my_choices[i+j*K] = 'p'
                    pt += P
                if tmp[j] == 's' and my_choices[i+(j-1)*K] != 'r':
                    my_choices[i+j*K] = 'r'
                    pt += R
                if tmp[j] == 'p' and my_choices[i+(j-1)*K] != 's':
                    my_choices[i+j*K] = 's'
                    pt += S

    print(pt)


if __name__ == '__main__':
    main()

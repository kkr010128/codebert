def main():
    N,K = map(int, input().split())
    R,S,P = map(int, input().split())
    T = list(input())
    score=0
    for i in range(N):
        if T[i] == 'r':
            score+=P
            if i+K<N and T[i+K]=='r':
                T[i+K]='x'
        if T[i]=='s':
            score+=R
            if i+K<N and T[i+K]=='s':
                T[i+K]='x'
        if T[i]=='p':
            score+=S
            if i+K<N and T[i+K]=='p':
                T[i+K]='x'
    print(score)







if __name__ == '__main__':
    main()
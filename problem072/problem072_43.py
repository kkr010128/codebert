if __name__ == '__main__':
    N = int(input())
    D = [input() for i in range(N)]    
    
    for i in range(2,N):
        if (D[i][0] == D[i][-1]) \
            and (D[i-1][0] == D[i-1][-1]) \
            and (D[i-2][0] == D[i-2][-1]):
                print('Yes')
                break
        if i == N-1:
            print('No')
if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    D = [0]*(N)
    for i, a in enumerate(A):
        D[a-1] = i+1
    
    print(*D)

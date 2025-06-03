if __name__ == '__main__':
    n, m, l = [int(i) for i in input().split()]
    A = [[int(i) for i in input().split()] for j in range(n)]
    B = [[int(i) for i in input().split()] for j in range(m)]
    B = list(map(list, zip(*B))) # trace
    C = [[sum(map(lambda x,y: x*y, A[i], B[j])) for j in range(l)] for i in range(n)]
    for i in C:
        print(' '.join([str(x) for x in i]))
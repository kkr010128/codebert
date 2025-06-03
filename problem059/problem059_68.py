# -*-coding:utf-8

def main():

    r, c = map(int, input().split())

    #A = [[0 for i2 in range(c+1)] for i1 in range(r+1)]
    A = []
    for i in range(r):
        tokens = list(map(int, input().split()))
        tokens.append(sum(tokens))
        A.append(tokens)

    rowSumList = []
    for i in range(c+1):
        rowSum = 0
        for j in range(r):
            rowSum += A[j][i]
        rowSumList.append(rowSum)

    A.append(rowSumList)

    for i in range(r+1):
        for j in range(c+1):
            if(j == c):
                print('%d' % A[i][j])
            else:
                print('%d ' % A[i][j], end='')

if __name__ == '__main__':
    main()
# -*-coding:utf-8

def main():

    n, m, l = map(int, input().split())
    A = []
    B = []

    for i in range(n):
        A.append(list(map(int, input().split())))

    for i in range(m):
        B.append(list(map(int, input().split())))

    Ans = []
    for i in range(n):
        row = []
        for j in range(l):
            rowSum = 0
            for k in range(m):
                rowSum += A[i][k] * B[k][j]
            row.append(rowSum)

        Ans.append(row)

    for i in range(n):
        print(' '.join([str(a) for a in Ans[i]]))

if __name__ == '__main__':
    main()
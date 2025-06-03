def calc_matrix(A, B, size):
    n, m, l = size
    # print(n, m, l)

    results = []
    for i in range(n):
        row_data = []
        for j in range(l):
            products = []
            for k in range(m):
                products.append(A[i][k] * B[k][j])
            # print('C[{0}][{1}] = {2}'.format(i, j, sum(products)))
            row_data.append(sum(products))
        results.append(row_data)
    return results


if __name__ == '__main__':
    # ??????????????\???
    A = []
    B = []
    # A.append([1, 2])
    # A.append([0, 3])
    # A.append([4, 5])
    # B.append([1, 2, 1])
    # B.append([0, 3, 2])
    n, m, l = [int(x) for x in input().split(' ')]
    for i in range(n):
        A.append([int(x) for x in input().split(' ')])
    for i in range(m):
        B.append([int(x) for x in input().split(' ')])

    # ???????????????
    results = calc_matrix(A, B, (n, m, l))

    # ???????????????
    for row in results:
        print(' '.join(map(str, row)))
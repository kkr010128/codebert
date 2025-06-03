from copy import deepcopy
import numpy as np
H, W, K = map(int, input().split())
matrix = []
for i in range(H):
    matrix.append(input())

matrix_int = np.ones((H, W), dtype=np.uint8)
# 1 == 黒、 0 == 白
for row in range(H):
    for column in range(W):
        if matrix[row][column] == ".":
            matrix_int[row, column] = 0

count = 0
for row_options in range(2**H):
    for col_options in range(2**W):
        tmp_matrix_int = deepcopy(matrix_int)
        tmp_row_options = row_options
        tmp_col_options = col_options

        for row in range(H):
            mod = tmp_row_options % 2
            if mod == 0:
                tmp_matrix_int[row,:] = 0
            tmp_row_options = tmp_row_options // 2
        
        for col in range(W):
            mod = tmp_col_options % 2
            if mod == 0:
                tmp_matrix_int[:,col] = 0
            tmp_col_options = tmp_col_options // 2
        # print(tmp_matrix_int.sum())
        if tmp_matrix_int.sum() == K:
            count += 1
print(count)
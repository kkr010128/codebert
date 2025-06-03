n, m, l = map(int, input().split())
A = [[int(num) for num in input().split()] for i in range(n)]
B = [[int(num) for num in input().split()] for i in range(m)]
B = list(zip(*B)) # 列を行に置き換える
C = [[0 for i in range(l)] for j in range(n)]
for i, A_line in enumerate(A):
    for j, B_line in enumerate(B):
        for A_element, B_element in zip(A_line, B_line):
            C[i][j] += A_element * B_element

for line in C:
    for i, element in enumerate(line):
        if i == l - 1:
            print(element)
        else:
            print(element, end=' ')


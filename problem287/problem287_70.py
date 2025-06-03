# B-81

# 標準入力 N

N = int(input())
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
j = 0

for i in range(1, 9 + 1):
    if (N / i) in num_list:
        j += 1

if j == 0:
    print('No')
else:
    print('Yes')


N, A, B = map(int, input().split())

cont_num = A+B

k = N // cont_num
# print(k)

adjust_num = N - k*cont_num
add_blue = 0
if adjust_num >= A:
    add_blue = A
else:
    add_blue = adjust_num

print(k*A + add_blue)
num_of_squares = int(input())
written_values = [i for i in input().split(" ")]
flag = 0
for i in range(num_of_squares):
    if ((i + 1) % 2 != 0) & (int(written_values[i]) % 2 != 0):
        flag += 1
print(flag)

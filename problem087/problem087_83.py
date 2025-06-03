n = input()
sum_of_digits = 0
for d in n:
    sum_of_digits += int(d)
print('Yes' if sum_of_digits%9 == 0 else 'No')
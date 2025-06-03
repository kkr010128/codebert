first_line = input()
length = int(first_line)
second_line = input()
numbers_str = second_line.split()
result_list = numbers_str[::-1]
result = " ".join(result_list)
print(result)

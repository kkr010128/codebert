input_lists = list(input().split(' '))
result = [input_lists[-1]]
result += input_lists[0:-1]
result = ' '.join(result)
print(result)
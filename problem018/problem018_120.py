input_list = list(map(str, input().split()))
stack_list = []

for i in input_list:
    if i not in ['+', '-', '*']:
        stack_list.append(i)
    else:
        a = stack_list.pop()
        b = stack_list.pop()
        stack_list.append(str(eval(b + i + a)))

print(stack_list[0])


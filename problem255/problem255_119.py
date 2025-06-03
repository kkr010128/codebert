length = int(input())
first_string, second_string = input().split()
first_list = list(first_string)
second_list = list(second_string)
result_list = []
for i in range(length):
  result_list.append(first_list[i])
  result_list.append(second_list[i])
  
result = "".join(result_list)
print(result)

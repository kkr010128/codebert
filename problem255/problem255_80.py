N = int(input())
list1,  list2 = input().split()
str = ''

for i, j in zip(list1, list2):
  str += f'{i}{j}'

print(str)
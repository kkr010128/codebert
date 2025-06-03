how_many = int(input())
results = []
index = 0
numbers = {index+1:int(item) for index,item in zip(range(how_many),input().split())}
for key_value in numbers.items():
  if key_value[0] % 2 == 1 and key_value[1] % 2 == 1:
    results.append(True)
print(len(results))

n = int(input())

num = [1,1]

for i in range(2,45):
  f = num[i - 1] + num[i - 2]
  num.append(f)
  
print(num[n])

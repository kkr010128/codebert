num = input().split()
x = [int(num) for num in num]
for i in range(5):
  if x[i] == 0:
    print(i+1)
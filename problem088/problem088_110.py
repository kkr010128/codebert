n = int(input())
input_line = input().split()
member = [int(input_line[i]) for i in range(n)]

stands = 0
for i in range(1,n): 
  stand = member[i-1] - member[i]
  if stand > 0:
    stands += stand
    member[i] += stand
print(stands)
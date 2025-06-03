N = int(input())
c = input()

num_red = c.count('R')
print(num_red - c[:num_red].count('R'))
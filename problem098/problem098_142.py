N = int(input())
#stones = list(input())
stones = input()
#print(stones)
a = stones.count('W')
b = stones.count('R')
 
left_side =stones.count('W', 0, b)
 
print(left_side)
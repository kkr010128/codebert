N= int(input())
stone_str = input()
r_cnt = stone_str.count('R')
print(stone_str.count('W', 0, r_cnt))
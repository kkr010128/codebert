N = int(input())
s = input()
r_count = s.count('R')
new_s = s[:r_count]
print(new_s.count('W'))

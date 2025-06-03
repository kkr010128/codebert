n = int(input())
s = input()

num_r = s.count("R")
count = 0

for i in range(num_r):
    if s[i] != "R":
        count += 1
    
print(count)
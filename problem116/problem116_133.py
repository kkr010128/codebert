s = input()
t = input()

count = 0
for l in range(len(s)):
    if s[l] != t[l]:
        count += 1
    
print(count)

s = input()
count = 0
max = 0

for i in range(len(s)):
    if s[i] == 'S':
        count =0
    else:
        count += 1
        if count > max:
            max = count

print(max)
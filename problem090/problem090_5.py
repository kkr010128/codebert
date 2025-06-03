s = input()
cnt = 0

if s == 'RSR':
    cnt = 1
else:
    for i in range(3):
        if s[i] == 'R':
            cnt += 1
    
print(cnt)
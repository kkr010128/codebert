s = input()
cnt = 0
for x in range(2):
    if s[x] == 'R' and s[x+1] == 'R':
        cnt += 1

for x in s:
    if x == 'R':
        cnt += 1
        break

print(cnt)
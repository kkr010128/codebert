a = input('')
S = []
num = 0
for i in a:
    S.append(i)
for j in range(3):
    if S[j] == 'R':
        num += 1
if num == 2 and S[1] == 'S':
    print(1)
else:
    print(num)
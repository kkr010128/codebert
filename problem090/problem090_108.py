S = input()
count = 0

if S[0] == 'R' or S[1] == 'R' or S[2] == 'R':
    count = 1

if (S[0] == 'R' and S[1] == 'R') or (S[1] == 'R' and S[2] == 'R'):
    count = 2
if S[0] == 'R' and S[1] == 'R' and S[2] == 'R':
    count = 3

print(count)
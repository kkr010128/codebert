n = int(input())

s = list(input())

count_red = s.count('R')
count_white = 0

A = []
for i in range(n):
    if s[i] == 'R':
        count_red -= 1
    if s[i] == 'W':
        count_white += 1
    A.append(max(count_red, count_white))

if len(set(s)) == 1 and list(set(s)) == ['W']:
    print(0)
else:
    print(min(A))
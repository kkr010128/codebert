import sys

input()
card = sys.stdin.readlines()
bool_ = [[False for y in range(13)] for x in range(4)]

for i in card:
    m, n = i.split()
    m = m.replace('S', '0').replace('H', '1').replace('C', '2').replace('D', '3')
    m, n = int(m), int(n)
    bool_[m][n - 1] = True

for i in range(4):
    for j in range(13):
        if not bool_[i][j]:
            if i == 0:
                print('S', j + 1)
            elif i == 1:
                print('H', j + 1)
            elif i == 2:
                print('C', j + 1)
            else:
                print('D', j + 1)
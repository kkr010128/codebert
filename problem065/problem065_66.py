import sys

W = sys.stdin.readline().strip()
num = 0

while True:
    T = sys.stdin.readline().strip()
    if T == 'END_OF_TEXT':
        break
    t = T.lower()
    T_line = t.split()
    for i in T_line:
        if W == i:
            num += 1

print(num)

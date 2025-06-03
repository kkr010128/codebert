import sys

input_num = int(sys.stdin.readline())

ans = ''
for i in range(3, input_num + 1):
    if i % 3 == 0 or '3' in str(i):
        ans += ' ' + str(i)
print ans
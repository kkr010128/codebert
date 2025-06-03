from sys import stdin
n = int(input())
dict = {}
for i in range(n):
    line = stdin.readline()
    if line[0:6] == 'insert':
        dict[line[7:]] = 1
    else:
        if line[5:] in dict:
            print('yes')
        else:
            print('no')

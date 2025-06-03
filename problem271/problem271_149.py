a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n = int(input())
ss = input()
print(''.join([a[(a.index(s) + n) % 26] for s in ss]))
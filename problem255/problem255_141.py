import sys
input = sys.stdin.readline

n, (s, t) = int(input()), input()[:-1].split()
print(''.join(s[i] + t[i] for i in range(n)))
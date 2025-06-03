import sys
input = sys.stdin.readline

a, b = input()[:-1].split()
print(min(''.join(a for i in range(int(b))), ''.join(b for i in range(int(a)))))
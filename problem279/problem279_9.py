import sys
N = int(input())
S = input()
if N % 2 == 1:
    print('No')
    sys.exit()

if S[:N//2] == S[N//2:]:
    print('Yes')
    sys.exit()

print('No')
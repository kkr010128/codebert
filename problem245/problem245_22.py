import sys
N = int(input())
S = input()
array_S = list(S)

if not ( 3 <= N <= 50 and S.isupper() ): sys.exit()

count = 0
for I in range(N-2):
    if ''.join(array_S[I:I+3]) == 'ABC':
        count += 1
print(count)
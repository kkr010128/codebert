S = input()

if len(S) % 2 != 0:
    print('No')
    exit()

tmp = [S[i:i+2] for i in range(0, len(S), 2)]

for s in tmp:
    if s != 'hi':
        print('No')
        exit()

print('Yes')

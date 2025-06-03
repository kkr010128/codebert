S = list(map(str,input()))

for i in range(len(S)):
    S[i] = 'x'
print(''.join(map(str,S)))
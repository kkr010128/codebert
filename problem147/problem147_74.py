S = input()
T = input()
if len(S) != len(T) - 1:
    print('No')
    exit(0)
for n in range(len(S)):
    if S[n] != T[n]:
        print('No')
        exit(0)
print('Yes')
S = input()

if S[-1] != 's':
    S = S + 's'
elif S[-1] == 's':
    S = S + 'es'

print(S)
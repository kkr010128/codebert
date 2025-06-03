K = int(input())
S = list(input())


if len(S) <= K:
    print(''.join(S))
    
else:
    del S[K:len(S)]
    S = ''.join(S) + '...'
    print(S)
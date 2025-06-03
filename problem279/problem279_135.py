N = int(input())
S = input()

if N % 2 == 1:
    print('No')
else:
    print(['No','Yes'][S[:(N//2)] == S[(N//2):]])
N = int(input())
S = input()

print('Yes' if S[:len(S)//2] == S[len(S)//2:] else 'No')
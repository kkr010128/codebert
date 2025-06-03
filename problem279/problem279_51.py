N = int(input())
S = input()
n = int(N/2)
print('Yes' if N > 1 and S[:n] == S[n:] else 'No')
# B - ... (Triple Dots)
# K
K = int(input())
# S
S = input()

if K >= len(S):
    answer = S
else:
    answer = S[0:K] + '...'

print(answer)

K = int(input())
S = input()

if K < len(S):
    S = S[:K] + "..."
print(S)
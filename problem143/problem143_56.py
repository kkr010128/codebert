K = int(input())
S = input()
if K >= len(S):
    print(S)
elif K < len(S):
    print(S[:K] + "...")

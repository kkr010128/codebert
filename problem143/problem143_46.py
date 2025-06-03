import sys
K = int(input())
S = input()

if not ( 1 <= K <= 100 and isinstance(K,int) and S.islower() and 1 <= len(S) <= 100): sys.exit()

print(S) if len(S) <= K else print(S[:K]+"...")
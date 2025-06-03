N = int(input())
S = input()
print(f'{S if len(S)<=N else S[:N] + "..."}')
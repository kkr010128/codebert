n = input()
S = set(input().split())
S.discard(' ')

q = input()
T = set(input().split())
T.discard(' ')


U = S.intersection(T)

print(len(U))
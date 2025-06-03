n = int(input())
S = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))

Sset = set(S)
Tset = set(T)

print(len(Sset & Tset))

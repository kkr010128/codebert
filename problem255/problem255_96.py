N = int(input())
S, T = input().split()
assert len(S) == N
assert len(T) == N

print(''.join([s + t for s, t in zip(S, T)]))
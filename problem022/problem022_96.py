N = int(input())
S = list(map(int, input().split()))
Q = int(input())
T = list(map(int, input().split()))

S = set(S)
T = set(T)
C = list(S & T)
print(len(C))